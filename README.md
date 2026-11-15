# Folkin – Unified Table Language

*An AI skill for writing UTL and creating your own frames for table roleplay.*

By [Folkin.io](https://folkin.io) · Version 0.1.0 · Review draft · 15 November 2026

Write Unified Table Language and create or adapt frames for FRAME by Folkin. The skill supports personal and professional play, existing material, and user-defined Tools. The instructions are in English; ask the assistant to work in Danish or another language.

The source repository is [Tjaelfe/folkin-unified-table-language](https://github.com/Tjaelfe/folkin-unified-table-language). Changes to the skill and references are maintained here.

## Attribution

The skill always credits [Folkin.io](https://folkin.io) and requires the same visible credit in the material it produces:

> Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

## What is included

- [SKILL.md](SKILL.md): the entry point and working instructions.
- [UTL](references/utl.md): syntax, attachment, states, perspective, Focus, and Actions.
- [Frame design](references/frame-design.md): purpose, setting, pressures, Tag Trees, NPCs, and practical coverage.
- [Meta and Macro](references/meta-macro.md) and [Micro](references/micro.md): summaries of all the book's named loop types and the five dice procedures.
- [Tools](references/tools.md): working with arbitrary Tool descriptions, plus Health 1d6.
- [Safety](references/safety.md): Avoid, Fade, and Notes when relevant.
- Three original [examples](examples/notebook.md), including a proposed [frame without Tools](examples/the-last-ferry.md) and a [new Tool](examples/shared-supplies.md).
- [Sources](references/sources.md): book edition, scope, and reconciled differences from older drafts.

The full book and genre Resources catalogs are not included. Other book Tools need their actual procedures supplied when those procedures are not bundled here. An assistant should distinguish official rules, local choices, and new proposals.

## Try it

Where an AI application supports folder-based skills, the skill entry point is the `SKILL.md` in this folder, with its references and examples alongside it. Installation steps depend on the application and have not yet been verified for this prototype. Merely attaching one file is not evidence of a native installation.

The combined Markdown edition contains the same instructions, references, and examples for use as a single reference attachment. Ask the assistant to use it for the requested task. The application's handling of long attachments and instructions still needs to be checked in actual use.

Example requests:

> Use this skill to create a local fantasy frame for three adults and two hours of play. We want investigation and relationships. Propose Loops and explain the choices. No Tools.

> Turn this character description into a UTL notebook. Preserve unknown information and do not add numerical systems.

> Review our frame. Distinguish UTL errors, missing procedures, and valid local adaptations. Preserve our own Tools.

> Create a pedagogical frame about making room for each other's ideas. Distinguish the group's purpose from the characters' Focus.

## Maintenance

Edit `SKILL.md`, the relevant reference, or the example directly. Keep the source book and local adaptations distinct, preserve notebook terminology, and retain Folkin.io attribution. Increase `metadata.version` in `SKILL.md` when preparing a new version.

Run `python3 scripts/package.py` to check the package and generate a ZIP and a combined Markdown edition under `dist/`. Only skill content is included; development notes and packaging scripts are excluded from the skill ZIP. These generated files are not committed to the source repository.

## Review status

This is a reviewable first version. Platform installation, user trials, actual playtesting, and final publication terms are not claimed complete. No distribution license has been assigned by this prototype.

For release preparation, review the examples and depth of the references, test representative requests in the intended AI applications, and set the terms covering the package. The existing local alternative license draft has not been adopted automatically.
