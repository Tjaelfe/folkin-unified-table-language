#!/usr/bin/env python3
"""Check and package Folkin – Unified Table Language using Python's standard library."""

from pathlib import Path
import posixpath
import re
import zipfile


ROOT = Path(__file__).resolve().parents[1]
CREDIT = "Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io)."
FILES = [
    "README.md",
    "SKILL.md",
    "references/utl.md",
    "references/frame-design.md",
    "references/meta-macro.md",
    "references/micro.md",
    "references/tools.md",
    "references/safety.md",
    "references/sources.md",
    "examples/notebook.md",
    "examples/the-last-ferry.md",
    "examples/shared-supplies.md",
]
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def check():
    content = {name: (ROOT / name).read_text(encoding="utf-8") for name in FILES}
    entry = content["SKILL.md"]
    front = re.match(r"\A---\n(.*?)\n---\n", entry, re.S)
    if not front:
        raise ValueError("SKILL.md must begin with YAML frontmatter")
    name = re.search(r"^name: ([a-z0-9]+(?:-[a-z0-9]+)*)$", front[1], re.M)
    version = re.search(r'^  version: "(\d+\.\d+\.\d+)"$', front[1], re.M)
    description = re.search(r"^description: (.+)$", front[1], re.M)
    if not name or name[1] != ROOT.name or len(name[1]) > 64:
        raise ValueError("The skill name must match the folder name")
    if not version or not description or len(description[1]) > 1024:
        raise ValueError("A version and a description of at most 1024 characters are required")
    for path, text in content.items():
        if CREDIT not in text:
            raise ValueError(f"Missing Folkin.io credit: {path}")
        if re.search(r"tagbook|/Users/|/private/tmp/|\[TODO:|\bTBD\b", text, re.I):
            raise ValueError(f"Obsolete terminology, private path, or unfinished content: {path}")
        if text.count("```") % 2:
            raise ValueError(f"Unbalanced code fences: {path}")
        for _, target in LINK.findall(text):
            if "://" in target or target.startswith("#"):
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), target.split("#")[0]))
            if resolved not in content:
                raise ValueError(f"Unpackaged or broken link in {path}: {target}")
    return name[1], version[1], content


def combined_document(name, version, content):
    anchors = {p: re.sub(r"[^a-z0-9]+", "-", p.lower()).strip("-") for p in FILES}
    sections = [
        "# Folkin – Unified Table Language\n\n"
        "*An AI skill for writing UTL and creating your own frames for table roleplay.*\n\n"
        f"Version {version} · Review draft\n\n{CREDIT}\n\n"
        "This combined edition contains the skill instructions, references, and examples. "
        "Use the skill instructions for the requested task and consult the relevant sections. "
        "Attaching this document is separate from a native skill installation.\n"
    ]
    for path in FILES:
        text = content[path]
        if path == "SKILL.md":
            text = re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S).lstrip()

        def link(match):
            label, target = match.groups()
            if "://" in target or target.startswith("#"):
                return match[0]
            destination = posixpath.normpath(posixpath.join(posixpath.dirname(path), target.split("#")[0]))
            return f"[{label}](#{anchors[destination]})"

        text = LINK.sub(link, text)
        lines, in_fence = [], False
        for line in text.splitlines():
            if line.startswith("```"):
                in_fence = not in_fence
            if not in_fence and re.match(r"^#{1,5} ", line):
                line = "#" + line
            lines.append(line)
        sections.append(f'<a id="{anchors[path]}"></a>\n\n' + "\n".join(lines) + "\n")
    document = "\n---\n\n".join(sections)
    ids = set(re.findall(r'<a id="([^"]+)"', document))
    for _, target in LINK.findall(document):
        if target.startswith("#") and target[1:] not in ids:
            raise ValueError(f"Broken combined-document anchor: {target}")
    return document


def main():
    name, version, content = check()
    document = combined_document(name, version, content)
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    archive = output / f"{name}-v{version}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as package:
        for path in FILES:
            package.write(ROOT / path, f"{name}/{path}")
    with zipfile.ZipFile(archive) as package:
        if package.testzip() is not None:
            raise ValueError("ZIP integrity check failed")
        for path in FILES:
            if package.read(f"{name}/{path}") != (ROOT / path).read_bytes():
                raise ValueError(f"ZIP content differs from source: {path}")
    single = output / f"{name}-v{version}-combined.md"
    single.write_text(document, encoding="utf-8")
    print(f"Checked {len(FILES)} package files, internal links, and Folkin.io attribution.")
    print(archive)
    print(single)


if __name__ == "__main__":
    main()
