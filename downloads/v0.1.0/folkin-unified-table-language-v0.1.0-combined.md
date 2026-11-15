# Folkin – Unified Table Language

*An AI skill for writing UTL and creating your own frames for table roleplay.*

Version 0.1.0 · Review draft

Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

This combined edition contains the skill instructions, references, and examples. Use the skill instructions for the requested task and consult the relevant sections. Attaching this document is separate from a native skill installation.

---

<a id="readme-md"></a>

## Folkin – Unified Table Language

*An AI skill for writing UTL and creating your own frames for table roleplay.*

By [Folkin.io](https://folkin.io) · Version 0.1.0 · Review draft · 15 November 2026

Write Unified Table Language and create or adapt frames for FRAME by Folkin. The skill supports personal and professional play, existing material, and user-defined Tools. The instructions are in English; ask the assistant to work in Danish or another language.

The source repository is [Tjaelfe/folkin-unified-table-language](https://github.com/Tjaelfe/folkin-unified-table-language). Changes to the skill and references are maintained here.

### Attribution

The skill always credits [Folkin.io](https://folkin.io) and requires the same visible credit in the material it produces:

> Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

### What is included

- [SKILL.md](#skill-md): the entry point and working instructions.
- [UTL](#references-utl-md): syntax, attachment, states, perspective, Focus, and Actions.
- [Frame design](#references-frame-design-md): purpose, setting, pressures, Tag Trees, NPCs, and practical coverage.
- [Meta and Macro](#references-meta-macro-md) and [Micro](#references-micro-md): summaries of all the book's named loop types and the five dice procedures.
- [Tools](#references-tools-md): working with arbitrary Tool descriptions, plus Health 1d6.
- [Safety](#references-safety-md): Avoid, Fade, and Notes when relevant.
- Three original [examples](#examples-notebook-md), including a proposed [frame without Tools](#examples-the-last-ferry-md) and a [new Tool](#examples-shared-supplies-md).
- [Sources](#references-sources-md): book edition, scope, and reconciled differences from older drafts.

The full book and genre Resources catalogs are not included. Other book Tools need their actual procedures supplied when those procedures are not bundled here. An assistant should distinguish official rules, local choices, and new proposals.

### Try it

Where an AI application supports folder-based skills, the skill entry point is the `SKILL.md` in this folder, with its references and examples alongside it. Installation steps depend on the application and have not yet been verified for this prototype. Merely attaching one file is not evidence of a native installation.

The combined Markdown edition contains the same instructions, references, and examples for use as a single reference attachment. Ask the assistant to use it for the requested task. The application's handling of long attachments and instructions still needs to be checked in actual use.

Example requests:

> Use this skill to create a local fantasy frame for three adults and two hours of play. We want investigation and relationships. Propose Loops and explain the choices. No Tools.

> Turn this character description into a UTL notebook. Preserve unknown information and do not add numerical systems.

> Review our frame. Distinguish UTL errors, missing procedures, and valid local adaptations. Preserve our own Tools.

> Create a pedagogical frame about making room for each other's ideas. Distinguish the group's purpose from the characters' Focus.

### Maintenance

Edit `SKILL.md`, the relevant reference, or the example directly. Keep the source book and local adaptations distinct, preserve notebook terminology, and retain Folkin.io attribution. Increase `metadata.version` in `SKILL.md` when preparing a new version.

Run `python3 scripts/package.py` to check the package and generate a ZIP and a combined Markdown edition under `dist/`. Only skill content is included; development notes and packaging scripts are excluded from the skill ZIP. These generated files are not committed to the source repository.

### Review status

This is a reviewable first version. Platform installation, user trials, actual playtesting, and final publication terms are not claimed complete. No distribution license has been assigned by this prototype.

For release preparation, review the examples and depth of the references, test representative requests in the intended AI applications, and set the terms covering the package. The existing local alternative license draft has not been adopted automatically.

---

<a id="skill-md"></a>

## Folkin – Unified Table Language

An AI skill for writing UTL and creating your own frames for table roleplay.

### Always credit Folkin.io

Whenever using this skill, include a visible credit to **Folkin.io** in the final response and in each deliverable created or substantially revised with it. Use this short credit, adapted only to the output format:

> Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

For plain text, write `Based on FRAME and Unified Table Language by Folkin.io. https://folkin.io`. Put the credit outside fictional notebook entries or rules so it is clearly attribution. Downloadable artifacts must contain the credit themselves; chat text or hidden metadata alone is insufficient. Preserve the credit when translating, revising, combining, or exporting material.

Help the user turn an idea into material they can use at the table. FRAME is a system for creating frames for table roleplay. A frame combines a purpose, participants, Loops, setting, and any selected Tools. UTL is its shared descriptive language.

Write in the user's requested language. Retain established FRAME terms and UTL symbols where translation would obscure their meaning. Use ordinary Markdown and fenced `text` blocks for UTL unless the user requests another format. No particular app, account, plugin, or book file is required.

### Choose the work

- **Write or revise UTL:** Read [UTL](#references-utl-md). Produce or edit the requested material at the requested scope. Preserve established fiction, perspective, ownership, unknowns, and states.
- **Design or adapt a frame:** Read [Frame design](#references-frame-design-md), [Meta and Macro Loops](#references-meta-macro-md), and [Micro Loops](#references-micro-md). Read UTL when writing the frame's playable material.
- **Write Actions or work with Tools:** Read [UTL](#references-utl-md) and [Tools](#references-tools-md). Read Micro Loops before specifying a roll or interpreting an outcome. A Tool's name or die size does not establish its procedure.
- **Review existing material:** Read the reference for the part being reviewed. Identify concrete problems and make the requested corrections. Separate a rule error from a valid local adaptation or a matter of taste.
- **Work with explicit boundaries:** Read [Safety notation](#references-safety-md) when entries are supplied or the chosen Meta Loop calls for them.

Examples: [a notebook](#examples-notebook-md), [a frame without Tools](#examples-the-last-ferry-md), and [a user-defined Tool](#examples-shared-supplies-md). They demonstrate possibilities, not mandatory forms or official additional rules.

### Establish enough context

Use the conversation and supplied documents first. A small UTL task rarely needs a complete frame questionnaire. Ask only for missing information that changes the requested result. For creative choices, offer a coherent draft and identify material assumptions; do not silently invent missing established facts when reading or reorganizing a document.

For mechanics, identify the selected Micro Loop and relevant Tool procedures. Distinguish **Tools not specified** from **no Tools selected**. Do not infer active Tools from a genre, a number in brackets, a weapon, or a reference file that happens to be present.

### Preserve FRAME's distinctions

- UTL describes what matters; it is not a fixed character sheet or a quota of entries.
- Tags describe fiction. Do not add universal numerical bonuses, attributes, Health, mana, progression, or costs unless the frame uses the corresponding procedures.
- General, Domain, and Niche express breadth, not prerequisites or automatic acquisition.
- A Relation's Tags belong to that Relation and its subject's perspective. They are not automatically the subject's personal abilities.
- A Focus can remain a question, hope, fear, or tension. Do not force every Focus into a mission or measurable success criterion.
- Actions and Tools are optional. Use only those selected for this frame, including user-defined ones. Keep a counter die separate from the Micro Loop's resolution dice.
- The Meta Loop remains active throughout play. Macro phases occur within the fiction; a Macro Reflection is different from an offgame reflection break.
- Prepare situations, pressures, and people who can respond to player choices. Leave room for the frame to develop through play.

### Source and local choices

The bundled references summarize the book identified in [Sources](#references-sources-md). Use them as the default for what this skill calls the book's rules. Clearly identify a supplied local variant or a newly proposed rule. An explicit local choice governs that frame without becoming a universal FRAME rule.

If a supplied source conflicts with a bundled rule, describe the specific difference. Ask for a decision only when the task depends on it; otherwise continue with the unaffected work. Do not invent the contents of a Tool or book section that is not included here. Preserve exact established names unless asked to rename them.

### Deliver and check

Deliver the requested artifact, not only advice about creating it. For a full frame, include enough setup, fictional material, procedures, and Leader guidance for someone else to begin play. Scale detail to the intended session and audience; avoid filling a template with irrelevant fields.

Before delivery, check UTL parentage and states, the perspective of Relations, consistency of Focus, the actual selected Loops, and every Tool value or Action outcome used. Check that a phase has a way forward and that a proposed ending does not depend on one prescribed player choice. State any assumptions or unresolved decisions that materially affect use. Do not claim a frame has been playtested merely because its text has been reviewed.

---

<a id="references-utl-md"></a>

## Unified Table Language

Source: the book's Word Definitions, pp. 22–24, and UTL chapter, pp. 31–50. See [Sources](#references-sources-md) for edition and editorial distinctions.

### Entries and attachment

UTL records meaningful fiction on a blank page or in a notebook. The book defines a **Notebook** as the ongoing record of a player or non-player character's identity and development, containing their Tags, Props, Relations, Focus, and Actions. Use a symbol followed by a short name; a colon can introduce a description. There is no compulsory order, fixed entry count, or universal set of character statistics.

| Symbol | Meaning |
| --- | --- |
| `#Tag` | What a character, object, Relation, or other subject is, knows, can do, or is affected by. |
| `+Prop` | A significant object, asset, or resource. |
| `-Note` | Supporting detail, limitation, instruction, or value attached to another entry. |
| `±Nested Prop` | A Prop contained in another Prop. |
| `@Relation` | A meaningful connection from the notebook subject's point of view. |
| `=Focus` | A direction, intention, question, concern, or other thing that matters. |
| `≠Focus` | Achievement: a Focus that has been achieved, abandoned, answered, or otherwise resolved. |
| `>Action` | An optional procedure for a recurring situation in the Micro Loop. |
| `?` | Existing but unidentified or undefined information. |
| `(entry)` | An entry that remains recorded but is inactive, unavailable, hidden, or lost. |

Use indentation to show attachment. For readable plain-text output, keep an entry's Tags on that entry's line. Indent its Notes beneath it. A Note beneath a nested Prop has an additional indentation level. These layout choices preserve parentage when the text is copied.

```text
+Travel Case: A battered wooden case.
  -Owner: The ferry crew.
  ±Lantern: Glass protected by a wire cage. #Weatherproof
    -Fuel: Enough for tonight.
  ±Rope: Fifteen meters of hemp rope.
@Edda: She gave me work when no one else would. #Grateful
=Question: Why did the north-bank bell stop ringing?
```

`Fuel` and `Owner` are open Note names, not mandatory fields or standardized resource systems. Keep existing labels unless a requested change justifies renaming them.

### Tags and breadth

Use concrete qualities and capabilities that can matter in play. Tags may help, hinder, establish a possibility, or have no mechanical effect in the current situation. The Leader decides which Tags apply under the selected Micro Loop.

Separate levels of breadth with `|`: General, Domain, Niche. For example, `#Craft`, `#Craft|Woodworking`, and `#Craft|Woodworking|Boatbuilding` are three separate choices. A narrower Tag does not require or grant the broader Tags.

Keep notebook Tags concise. Put surrounding background in prose where useful. In a Tag Tree or explanatory collection, descriptions explain the available choices. The book's glossary allows Notes attached to Tags as well as Props, Relations, Focus, and Actions; do not turn a particular example's bare-Tag presentation into a universal prohibition on supporting Notes.

An actual title can be written `#Title|Harbor Warden`. A generic class label is rarely as useful as the abilities, qualities, or position that matter in this frame. A character may have several relevant Tags or very few; their life and role determine the detail.

Some frames explicitly assign values to Tags. Do not use `#Agility +2` as a default character model. A shared numerical attribute system requires its own selected Tool or defined local procedure. The UTL symbol alone never specifies a modifier rule.

### Props, contents, and Notes

Props can be belongings, shared resources, places, equipment, spells, or other assets. Add Tags when the qualities matter and Notes when details or selected Tools need them. Do not catalog every ordinary feature.

Use `±` for a contained Prop and `-` for supporting information. A rope inside a case is a Prop; the case's carrying restriction is a Note. When the rope is recorded separately, change its marker to `+` and preserve its description, Tags, and Notes. Moving it does not duplicate it.

The current book places a nested Prop's Notes on separate indented lines. Older material may keep them on the same line. Read such material without losing attachment; use the current structure for new output.

Books may also record spells or recipes as Notes in existing material. Do not convert every such Note into a Prop automatically. When asked to standardize independent contained Props, use `±` and preserve their information.

Mechanical values are contextual. `-Damage: 2`, `-Protection: 3`, and `-Reduction: 3` do not by themselves select a Tool or guarantee identical mechanics. A Prop can be useful without any numerical values.

### Values, levels, and unknowns

A value in brackets follows the entry's name, for example `+Working [2]` or `+Working [X]`. It may express a cost, level, or another frame-defined value. Its meaning comes from the frame or selected Tool. It is not automatically damage, a spell slot, or an attribute bonus.

Determine X before calculating an effect that depends on it. Follow the entry's definition of what varies. If it supplies no measure, the Leader and player agree on X from the intended effect where the selected procedure allows this. Do not silently make every aspect of an effect scale with X. Keep an explicitly supplied combined value such as `[1 / X]` and obtain its definition when its use matters.

`#?`, `#Magic|?`, and `@?: Someone has been leaving food at my door.` preserve uncertainty. Do not replace the unknown part with invented established knowledge during transcription or review.

### Relations

Relations can concern people, groups, creatures, places, institutions, or other entities with personal meaning. A Relation records what the entity means to the notebook's subject. Two people can record the same entity differently without contradiction.

```text
Arin
@Edda: She always hears me out. #Trusted

Vale
@Edda: She remembers every favor I owe. #Wary
```

Neither Relation gives Arin or Vale a personal `#Trusted` or `#Wary` ability. In the book's example, if Arin trusts Edda, Edda may use that relational trust when interacting with Arin. The Leader may also allow Arin to use it when the fiction makes it relevant. Avoid reversing who trusts whom.

### Focus and change

Focus can belong to a player, character, NPC, or group. Keep an out-of-fiction purpose distinct from a character's intention: a player can explore betrayal through a character devoted to loyalty.

Use labels suited to the intention, such as `=Hope`, `=Question`, `=Task`, or `=Intention`. They are examples, not a closed taxonomy. Resolving a Focus changes `=` to `≠`; retain the entry as history and describe how it ended when that is useful. Resolution includes abandonment or failure, not only success.

Parentheses preserve an unavailable element: `(+Rope)` or `(#Melee)`. A passive Tag contributes no positive roll bonus, though its history may still matter in the fiction. Remove parentheses when the relevant fictional change makes the entry active again. Do not reactivate something merely to improve a roll.

### Actions

Read [Micro Loops](#references-micro-md) before specifying or resolving a rolled Action. A character declaring an act is not automatically using a defined `>Action`.

An Action needs a recognizable name and fictional trigger. It uses only the automatic effects, outcomes, and choices it needs:

| Marker | Meaning |
| --- | --- |
| `A:` | Automatic effect when triggered. The marker is optional; the effect may be in the trigger sentence. |
| `S:` | Shine: exceptional success or an additional advantage. |
| `P:` | Positive: success as intended. |
| `T:` | Trade: success with a cost, complication, choice, or reduced effect. |
| `N:` | Negative: failure, unwanted result, or complication. |
| `D:` | Dire: catastrophic failure that substantially worsens the situation. |
| `-` under an outcome | Choices or instructions attached to that outcome. Follow its stated number of choices. |

An Action may be Auto only and require no roll. If an outcome is not specified, use the selected Micro Loop and established fiction. Do not demand all six markers or automatically add a mana, ammunition, or damage system.

The book uses `roll +/- #` as a generic trigger ending. Where writing for the 1d6 loop, explain its actual one-reroll procedure rather than turning Tags into numerical modifiers. A proposed Action must fit its frame's actual loop.

### Shared notebooks

A shared notebook can record group circumstances, assets, Relations, and Focus alongside individual character notebooks. A shared reputation can matter when the group is recognized; it does not automatically give every member the same skills. Access to a shared Prop follows its location and the fiction. A group Relation can differ from an individual's Relation to the same person.

This is an application of the project's working text on a shared group record. It does not establish a new official notebook type, universal party bonus, or required group sheet.

Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

---

<a id="references-frame-design-md"></a>

## Design a Frame

Source: Design, pp. 259–301. The book treats design as connected choices: begin with purpose and move between Loops, Tools, setting, and fictional material as they inform one another. Prepare enough to start; develop the frame through play.

### Start with the intended experience

Find out who will play, what they want to experience or work with, and the practical conditions. Time, experience, familiarity, age, and desired complexity matter when they change the design. Use information already supplied. A short creative brief can support an initial proposal; ask a small number of questions when a missing choice would change the whole frame.

Name the purpose in ordinary language. For professional work, keep its out-of-fiction Focus clear and distinguish it from what the characters want. Do not infer a therapeutic purpose from an emotional theme or impose a learning goal on personal play.

### Assemble the frame

Use [Meta and Macro Loops](#references-meta-macro-md) and [Micro Loops](#references-micro-md) to choose and explain the structures. A useful rationale connects each choice to what players will actually do. Avoid genre-only claims such as "fantasy requires 2d6" or "professional play always uses Care."

Choose [Tools](#references-tools-md) only for a recognizable need. Zero Tools is a complete choice. A custom Tool can be simpler and more appropriate than assembling several book Tools. Document local adaptations so someone else can use them.

For a full frame, provide the following where useful, in an arrangement suited to the user:

- Purpose, intended participants, approximate duration, and premise.
- Selected Loops, their rationale, and the actual Macro transitions.
- Active Tools and Actions, with their procedures; or an explicit choice of no Tools.
- The setting, immediate pressures, important people, and starting situation.
- Character preparation: suitable concepts or prepared notebooks and meaningful connections.
- Enough Leader guidance to begin, respond to approaches, and handle likely consequences.
- The Meta opening and ending, including reflection suited to the purpose.

This is a coverage guide, not a compulsory published template. A requested NPC or short setting seed needs only its relevant parts. Do not call an outline ready to play when essential procedures or starting material are still missing.

### Create the setting

Choose scope. A **Global Setting** offers a wider world within which many local places and stories can belong. A **Local Setting** develops a particular village, district, station, forest, or other corner of a world. The wider world may be familiar reality or an established fictional setting; describe only the surrounding context needed here.

Give players a clear silhouette: recognizable genre elements, tone, significant differences from ordinary expectations, and room to contribute. List the factions, places, people, resources, customs, authorities, threats, and strange elements that matter now. Do not fill every category or write a world encyclopedia for a short session.

#### Tensions

Begin with a situation that cannot remain as it is. Establish who wants what, why it matters now, what resists them, and what may happen without intervention. Connect it to the characters and allow several responses.

- **Near:** Inner conflicts and immediate relationships.
- **Concrete:** An actionable threat, problem, or unresolved question.
- **Looming:** Wider pressures that can emerge over several sessions.
- **Symbolic:** A contrast such as continuity and change, made visible through people, places, and decisions.

Use only the kinds needed. Offer pressures and possible consequences rather than a prewritten sequence that demands particular character decisions. A story direction can guide preparation while the route and meaning emerge in play.

### Select a Tag Tree

Identify the activities characters are likely to undertake, including ordinary work and relationships as well as conflict. Gather or write Tags that support those activities, adapt the choices to the setting, and try a few plausible character concepts to find gaps or irrelevant abundance.

An **open** tree permits proposed additions that fit and receive the Leader's agreement. A **locked** tree limits choices to the supplied collection. State which is used. Tags at different breadths are separate choices, with no prerequisite or automatic acquisition rule.

Provide descriptions in a Tag Tree to explain the choices. In the resulting character notebooks, record the selected Tags themselves. The book's Resources collections can inspire choices when the user supplies them, but this package does not contain or claim to reproduce the complete catalogs. Any new collection made for the task is proposed material.

### Create NPCs for their function

The function determines the detail. Do not require every NPC to have a fixed number of Tags, Relations, Props, or Actions.

| Type | Design question |
| --- | --- |
| Relational | What relationship can the player explore through the character? Give the NPC their own needs and put the relationship in a concrete situation. |
| Support | What help does the player need, and how can the NPC offer it to the character inside the fiction? Define what the NPC knows, offers, and why. |
| Plot | What does the NPC want, how can they pursue it, and how do their choices connect to the characters? Prepare a next move and responses to interference. |
| Trash | What immediate obstacle, pressure, or atmosphere does this figure create? Give enough attitude, capability, and response to sustain that scene. Develop more if play makes them recurring. |
| Monster | What danger and atmosphere does it create? Establish signs, capabilities, limits, and what happens if it is not interrupted. Define modes and transition triggers only if it has distinct modes. |

Write the relevant material using [UTL](#references-utl-md). Keep contextual explanation separate from the notebook's personal Tags. Use a defined Action only when a recurring situation needs that procedure.

### Check the design through a likely situation

Follow a plausible player choice from the opening through a phase transition, an uncertain act, its consequence, and the next opportunity. Also try refusal or an unexpected approach. Check that required clues or routes are not locked behind a single failed roll with no way forward.

Look for mechanical additions without a clear job, missing procedures, and preparation that assumes one ending. Review what the Leader must actually track. Keep only the handling that supports the intended experience. This is a design review; actual playtesting remains a separate step.

Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

---

<a id="references-meta-macro-md"></a>

## Meta and Macro Loops

Source: pp. 54–71, 76–93, 264–273. These are concise design guides, not reproductions of every diagram or every Leader responsibility.

### Meta Loop

The Meta Loop concerns the people, purpose, preparation, participation, and reflection. It remains active while fictional play continues. When everyone is offgame, play is exclusively in the Meta Loop. Never say the group leaves the Meta Loop to enter the fiction.

Choose according to purpose and participants, including time, experience, familiarity, and desired complexity. Personal play can be emotionally demanding or reflective. A fictional negotiation does not establish whether the frame is for adventure, group development, knowledge, or skill practice.

| Type | Design implications |
| --- | --- |
| Casual | Shared play and storytelling with friends. Introduce the setting and frame, create characters together, connect shared Focus, check readiness, then review the experience and notebook changes afterwards. |
| Minimal | A quick start with prepared characters and opening. Present their roles, connections, relevant procedures, and the setting. Retain a brief check-in, breaks, and an ending with feedback and Focus review. |
| Care | Build in explicit boundaries, care, check-ins, adjustments, and attention to intensity alongside character creation and play. |
| Pedagogical | Begin with a Group Focus about participation, relationships, or cooperation. Prepare roles and situations that let it matter. Observe interaction; use reflection breaks and evaluate the Group Focus after play. |
| Didactical | Begin with a Knowledge Focus. Connect the setting and prepared or jointly created characters to that knowledge. End by examining what participants understood, what surprised them, and what remains open. |
| Therapeutic | Work with an agreed Self Focus through fictional characters within an established therapeutic relationship. Character preparation, consent, reflection breaks, attention to emotional material, and evaluation follow that professional framework. |
| Training | Participants play themselves in a simulated context. Use a briefing and authentic notebooks based on relevant real strengths, vulnerabilities, resources, and relations. Define Team and Skill Focus; use practice, feedback, and evaluation. |
| Philosophical | Establish a Philosophical Field and each player's Question Focus. Prepare characters and dilemmas that support inquiry. Facilitate reflection while allowing defensible differences and unresolved questions. |

Differentiate Pedagogical from Didactical by the intended work: how the group participates versus understanding a defined area of knowledge. Cooperation may occur in both. Distinguish Training's authentic self from Therapeutic's work through a fictional character.

Plan an actual beginning and ending. Make clear how participants are introduced to the frame, how characters are prepared, when the Leader signals entry into the fiction, how pauses are handled, and what reflection serves the chosen purpose. Do not prescribe identical rituals for every group. Use [Safety](#references-safety-md) where the selected loop and circumstances call for explicit agreements.

A custom Meta Loop should explain its purpose, preparation, participant and Leader responsibilities, pauses, and ending. Mark the adaptation clearly instead of presenting it as another named book type.

### Macro Loop

The Macro Loop shapes recurring activity inside the fiction. Its phases are structures for play, not prescribed plot events. The book's types can be adapted, combined, reordered, or supplemented with new phases when they serve the frame.

The following lists summarize the book's phase sets. They do not mean that each phase occurs only once in a straight line. State the return paths and transitions for the frame being designed.

| Type | Phase set / characteristic movement |
| --- | --- |
| Standard | Free Play, Exploration, Encounter, Recovery. Discovery and focused pressure alternate; recovery reveals what changed. |
| Open | Introduction, Free Play, Exploration, Closure. Players follow curiosity and relationships toward a landing point. |
| Crawl | Introduction, Exploration, Encounter, Recovery. Explore connected places or resistance; after encounters, decide whether to continue, change direction, pause, or withdraw. |
| Prepared | Introduction, Planning, Encounter, Recovery. A clear objective meets resistance; changed conditions can return the group to Planning. |
| Inquiry | Introduction, Exploration, Encounter, Reflection, Large Encounter, Closure. Gather and interpret clues; return to Exploration until the inquiry reaches a decisive point. |
| Drama | Introduction, Free Play, Encounter, optional Hygge, Closure. Relationships drive the return between open interaction and moments that test or change a bond. |
| Survival | Introduction, Planning, Exploration, Encounter, Recovery. Scarcity and danger produce repeated choices; Recovery leads back to Planning. |
| Journey | Planning, optional Flash Forward, Mosaic, Exploration, Hygge, Encounter, Recovery. Travel moves between impressions, discovery, quiet life, and focused pressure. |

#### Phase meanings

- **Introduction:** Orient the characters to the situation, tone, and stakes.
- **Free Play:** Open interaction, character expression, and emergent activity.
- **Planning:** Characters coordinate intentions, approaches, roles, and resources inside the fiction.
- **Exploration:** Investigate places, people, objects, tensions, or possibilities.
- **Encounter:** Focused engagement with an immediate challenge or dramatic situation. Small is brief; Medium sustains a scene or short sequence; Large forms a major peak with several moving parts and lasting effects. These are not encounter difficulty ratings or synonyms for combat.
- **Recovery:** Regain stability, resources, trust, or emotional footing while consequences become visible.
- **Reflection:** Characters compare experiences, evidence, and interpretations within the fiction. This is different from an offgame Meta reflection break.
- **Closure:** Give the present movement a meaningful stopping point; not every issue must be resolved.
- **Hygge:** Low-pressure time for presence, relationships, and life inside the fiction, without a required objective.
- **Mosaic:** Sensory images, fragments, and passing moments that create atmosphere and transition.
- **Flash Forward:** Establish a future fictional event, then return to the present to discover how it happens. Use deliberately: it commits the fiction to that event.

#### Make it usable

For a custom Macro Loop, identify the activity the characters return to, choose the few phases that sustain it, describe the transitions and return paths, and run a likely situation through the pattern. Keep scene preparation responsive: players should have meaningful approaches, and refusal or failure must leave a way for play to continue.

Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

---

<a id="references-micro-md"></a>

## Micro Loops

Source: pp. 98–109 and 274–275. Use the dedicated procedures over loose descriptions of dramatic feel. One Micro Loop is selected for a frame. The group may design a local variant, which must be identified as such.

### Before any roll

The Micro Loop connects Invitation, Pre-Stance, Act or React, resolution, Post-Stance where used, and Consequence to the next Invitation. The player states the character's act in the first person. Doing nothing can also be an act.

- If failure is not relevant, proceed to Positive without rolling.
- If there is no chance of success, proceed to Negative without rolling.
- When success is possible and failure matters, consider relevant Tags and follow the selected dice procedure.

The Leader has final authority over applicable Tags. Only Tags relevant to this act count. An opponent's entire notebook is not a universal penalty. In the modifier loops, Tags from characters, NPCs, or the world can help or oppose as the fiction warrants. No general maximum number of Tags is imposed.

### Modifier loops

For 2d6, 2d8, 2d10, and 1d20, roll the indicated dice and add supporting Tags, subtracting opposing Tags. Other numerical modifiers apply only if selected Tools or local rules define them.

**Natural Dire and Shine take precedence over the modified total.** Check the dice themselves first; a natural Dire does not become Positive because of modifiers, and a modified high total is not automatically Shine.

| Loop | Natural Dire | Negative total | Trade total | Positive total | Natural Shine |
| --- | --- | --- | --- | --- | --- |
| 2d6 | Two 1s | 6 or less | 7–9 | 10 or more | Two 6s |
| 2d8 | Two 1s | 8 or less | 9–12 | 13 or more | Two 8s |
| 2d10 | Two 1s | 10 or less | 11–15 | 16 or more | Two 10s |
| 1d20 | 1 | 9 or less | 10–15 | 16 or more | 20 |

The dedicated modifier-loop diagrams also instruct that when Tags are insufficient in quantity or quality for the act, Positive is treated as Trade. This is a fictional judgment by the Leader, not a hidden difficulty number or a demand for a universal Tag quota. It does not override natural Dire or Shine.

### 1d6

Roll one d6 without a numerical Tag modifier:

| Die | Outcome |
| --- | --- |
| 1–2 | Negative |
| 3–4 | Trade |
| 5 | Positive |
| 6 | Shine |

With one relevant Tag accepted by the Leader, the player **may reroll once and must keep the new result**. The current procedure on p. 107 does not restrict this permission to an initial 1. More Tags do not grant more rerolls. There is no Dire. A 6 on the permitted reroll is Shine.

For example, an initial 3 is Trade. The player may keep it or use the relevant Tag to reroll. If the reroll is 2, the final outcome is Negative; the player cannot keep the earlier 3 instead. Older examples showing a reroll of 1 do not establish an only-on-1 restriction.

### Outcomes and Stances

Positive achieves the intended act. Trade achieves it with a cost, complication, hard choice, or reduced effect. Negative fails or creates an unwanted result. Shine exceeds the intended success. Dire substantially worsens the situation. Use the chosen Action's details when one applies.

Pre-Stance can be In Front, where the Leader prompts a reaction, or Behind, where players take initiative. In the modifier-loop diagrams, Post-Stance is In Front, Beside, or Behind: the Leader, both together, or the player describes the consequence. Stance allocates description and initiative; it does not change the outcome category.

Make consequences concrete and consistent with the act, available means, relevant Tags, and established stakes. A Dire or Shine is not by itself a rule granting a permanent new Tag. Record a lasting change when the fiction establishes one.

### Choosing or designing a loop

2d6 makes individual Tags more influential than the larger two-dice loops. 2d8 and 2d10 make smaller shifts per Tag and have rarer natural extremes. 1d20 has equally likely faces and natural Dire and Shine each occur on 1 in 20 rolls. 1d6 offers a short procedure with one relevant Tag and one optional reroll.

Do not describe 2d8 or 2d10 as automatically producing more frequent natural extremes than 2d6. Natural Dire and Shine each occur on 1 in 36, 64, and 100 rolls respectively. Genre and dramatic stakes also depend on the situations, Macro Loop, and consequences.

For a custom Micro Loop, define when to roll, the dice, Tag effects, all outcome boundaries, treatment of extremes, and how the outcome changes the fiction. Try likely acts with no Tags and with several relevant Tags. Do not silently substitute a familiar game system.

Worked checks: on 2d8, natural 2 and 5 with net +2 gives 9, Trade. On 2d6, natural 1 and 1 remains Dire with +10. On 1d20, natural 18 with +2 is Positive, not Shine.

Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

---

<a id="references-tools-md"></a>

## Tools and Frame Context

Source: pp. 276–277 and 341–343. Tools are optional procedures or aids selected for a frame. The book's examples are not a closed list.

### Read an existing or user-defined Tool

Use the supplied description even when the Tool is unfamiliar. Find the information the task needs: its purpose, preparation, trigger, who handles it, what changes, what the change means, and its connections to UTL, other Tools, or the selected Micro Loop. A Tool need not have numbers or dice.

Do not require a registry, configuration file, or software integration. Context may be in the conversation or an ordinary frame document. Ask for a missing procedural detail only when the current result depends on it. A note such as `-Supplies: 3` alone does not define a consumption rule.

Distinguish a **counter die**, which displays a changing value, from **resolution dice**, which are rolled for an uncertain act. Health 1d6 may be a counter in a frame that resolves acts with 2d8. A Tool mentioning its own explicit roll is not automatically translated to another Micro Loop: check the actual procedure and identify any proposed adaptation.

This prototype includes the Health procedure below. Other book Tools are not fully documented in this package. If asked to use one whose procedure is not supplied, obtain the relevant description instead of inventing its exact rules. A proposed new Tool must be clearly identified as new.

### Build or adapt a Tool

Identify the activity, condition, or decision that needs support. First consider whether existing Tags or a selected procedure already serve it. Define the preparation, trigger, handler, changes, effects, and connections. Keep the amount of handling proportional to its purpose.

Try ordinary use, an edge state, and recovery or reset where relevant. Check compatibility with the chosen Micro Loop and other active Tools. Provide an example that shows what changes in the fiction. The [Shared Supplies example](#examples-shared-supplies-md) demonstrates a complete new procedure with no registry or additional dice system.

### Health 1d6

Book Tool, pp. 342–343. Use only when selected.

Each character starts at a maximum of 6 Health, displayed on a visible d6. The die is a counter. Health describes physical condition:

| Health | Condition |
| --- | --- |
| 6 | Unharmed |
| 5 | Minor scratches |
| 4 | Noticeable wounds |
| 3 | Significant injury |
| 2 | Severe pain |
| 1 | Near collapse |

Damage and its consequences follow the fiction, the act, and the outcome. The book rates incoming damage intensity from 1 to 6; a weapon's Note may specify a value where the frame uses one. Do not assign automatic damage merely for entering an Encounter.

Protection only applies to relevant incoming harm. Add the relevant Reduction values and apply that total once. For an incoming damaging hit, at least 1 point gets through: `damage taken = max(1, incoming damage - applicable Reduction)`. This minimum does not create damage when no damaging event occurs. A Note called `Protection` is not automatically a defined Reduction value.

Examples: incoming 3 against Reduction 3 causes 1 Health loss; incoming 6 against two applicable reductions of 1 and 2 causes 3 Health loss. Fire Reduction does not reduce acid damage.

At 0 Health, hand the counter to the Leader and resolve **Face Death using the frame's selected Micro Loop**, with relevant Tags according to that loop:

| Outcome | Effect |
| --- | --- |
| Shine | Survive with 2 Health. |
| Positive | Survive with 1 Health. |
| Trade | Survive with 1 Health and choose one fitting consequence from Injury, Fear, or Debt. |
| Negative | Dying; choose two fitting consequences from the Trade list. Immediate help may still save the character. |
| Dire | Die, with an opportunity for last words. |

Injury adds a fitting Tag such as `#Limping`; Fear adds a fitting fear Tag; Debt adds or changes a Relation with `#Indebted`. The consequences must fit what occurred. With 1d6 resolution there is no Dire; do not add a death result that the selected loop cannot produce.

The Leader decides what rest, treatment, or healing restores according to the fiction. Health normally cannot exceed 6. The book does not supply a universal rest duration or fixed healing-per-hour rule here; do not invent one as a book rule.

Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

---

<a id="references-safety-md"></a>

## Safety Notation

Source: pp. 156–157. This extends UTL for explicit agreements when the Meta Loop and circumstances call for them.

| Marker | Meaning |
| --- | --- |
| `!!Topic` | Avoid: the content must not appear or be explored. |
| `!Topic` | Fade: the content may exist, but is not played out or described in detail. |
| `-Note` | A relevant consideration that Avoid or Fade does not express. |

```text
!!Possession
!Detailed injuries
-A participant may step away without explaining why.
```

These are examples, not default boundaries for all frames. Preserve the user's actual entries and distinctions. Participants do not need to explain why a boundary matters. If an entry affects material being written, change the detail, fade, redirect, or leave space for a pause as appropriate.

Match preparation to the people, purpose, trust, age, and professional relationship. A familiar group's brief check and a Care frame's explicit agreements need not use an identical form. Difficult fiction is not by itself a reason to remove a theme the table has agreed to explore. Do not invent personal boundaries for participants.

Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

---

<a id="references-sources-md"></a>

## Sources and Status

Version: 0.1.0, review draft, 15 November 2026. This package is a newly written working summary and original examples for review. It is not a replacement edition of the book or an assertion that the prototype has been approved or playtested.

### Primary book

**FRAME – Personal and Professional Table Roleplay**, Folkin, 2026. Source file: `FRAME - Personal and Professional Table Roleplay - A5 bogblok - v1o1.pdf`, 580 PDF pages, export 5 November 2026.

SHA-256: `72eabe32ba355aeab7d8f149041561f5e245d03347cf1f43a67c6fc67a4864e2`.

Page references here are printed book pages. The source PDF has 14 pages before printed page 1; printed page 42 is PDF page 56. This identifies the source; using the skill does not require the PDF or access to the publisher's working folders.

| Reference | Book basis |
| --- | --- |
| UTL | Word Definitions, pp. 22–24, and UTL, pp. 31–50: notebooks, syntax, Tags, Props, Notes, Nested, Relations, Focus, Achievement, Actions, passive elements. |
| Meta and Macro | pp. 54–71 and 76–93; design guidance pp. 264–273. |
| Micro | pp. 98–109 and 274–275. |
| Frame design | pp. 259–301: principles, design, Loops, Tools, setting, Tag Trees, tensions, and NPC types. |
| Tools | pp. 276–277 and 341–343; only Health 1d6 has a complete bundled book-Tool procedure. |
| Safety | pp. 156–157. |

Relevant diagram details on printed pp. 42 and 107 were also visually checked against the PDF during authoring. Summaries omit some detail from the book and should not be described as the complete book reference.

### Working materials used

The publisher's earlier architecture proposal supplied the UTL-first architecture, support for arbitrary user-defined Tools, source separation, and realistic evaluation scenarios. It is a development proposal, not a rule authority or a runtime dependency.

Project texts on Notes, Nested, frame design, Tag Trees, tensions, NPCs, shared group records, the genre Resources, and extended play examples informed the scope and presentation. Their presence does not make every draft a current book rule. The full genre catalogs, private feedback, and book PDF are not bundled.

The shared-notebook section adapts a working manuscript on group records as an application of UTL. It does not claim a separately published new Tool. Notebook examples keep Tags concise, while the current book's glossary permits Notes attached to Tags. Older example-specific editorial preferences are not presented as universal rules.

### Reconciled differences

- **Notebook:** the current book explicitly defines Notebook on p. 23. The earlier architecture proposal uses an obsolete name for that record; this package uses notebook throughout.
- **Nested Notes:** the current book, p. 42, puts Notes on separate lines under a nested Prop. The older standalone Nested manuscript and architecture proposal kept them on the same line. New examples follow the current book.
- **1d6 rerolls:** the current dedicated procedure, p. 107, allows one optional reroll with a relevant Tag and requires keeping the new result. Some older drafts restrict rerolls to a 1. This package follows p. 107 and does not apply that older restriction.
- **Natural extremes:** dedicated loop procedures and pp. 274–275 distinguish natural Dire and Shine. Older dramatic descriptions must not be used to infer different outcome boundaries or more frequent extremes for larger two-dice loops.
- **Health:** pp. 342–343 now state the selected Micro Loop for Face Death, a narrative Trade consequence, combined applicable Reduction, and at least 1 damage getting through. Do not restore the older contradictory fire-immunity example from the architecture proposal.
- **Tag Trees:** the later design text concerns selecting meaningful choices for a setting. Earlier drafts are not a basis for importing a progression tree or prerequisites.
- **Missing historical references:** the earlier beta-PDF path and `Bogindhold/Tools/Spell-Levels.md` named in the architecture proposal are not runtime dependencies. Bracket values are summarized from the current book rather than that missing supplement.

### New examples and publication

All files under `examples/` are newly written illustrative material for this prototype. Their people, places, time estimates, and local rules are proposals, not additional official FRAME rules. A proposed frame can be runnable while remaining unplaytested.

The prototype does not assign a publication or redistribution license. The project's alternative license draft was not adopted as the package's terms. Folkin's final distribution terms and platform-specific installation checks remain work for release preparation. The skill and its outputs must always visibly credit Folkin.io. The GitHub repository holds the development version; website publication and platform installation are separate steps.

Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

---

<a id="examples-notebook-md"></a>

## Example: A Ferry Mechanic

New illustrative material for this prototype. Frame context: contemporary local fiction with no numerical Tools selected. The resolution loop is not specified because this task only writes a notebook.

### Request

Write a notebook for a ferry mechanic who distrusts the harbor authority but feels responsible for her apprentice. She carries a toolbox, and her old workshop is inaccessible. Someone has been sending anonymous warnings.

### Draft

```text
Mara
#Craft|Repairs
#Observant
#Stubborn
@Iven: My apprentice takes risks to prove he can manage alone. #Protective
@Harbor Authority: They inspect our papers and ignore our warnings. #Distrust
@?: Someone sends me warnings before each closure.
+Toolbox: A dented metal case.
  ±Spanner: Worn smooth at the grip.
  ±Inspection Lamp: A bright light on a flexible lead.
(+Old Workshop): Sealed by the harbor authority.
=Intention: Keep Iven from taking the blame for the ferry's faults.
=Question: Who is warning me, and what do they want?
```

The draft adds proposed characterization through Tags; it preserves the sender as unknown. It does not infer Health, damage, attributes, a dice procedure, or a numerical repair bonus. The workshop remains recorded as unavailable. Mara's protectiveness belongs to her Relation to Iven; it is not Iven's ability.

If the lamp is taken out of the toolbox and recorded separately, move it to `+Inspection Lamp: A bright light on a flexible lead.` Remove its nested entry from the toolbox. Its description and any later Tags or Notes travel with it.

Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

---

<a id="examples-the-last-ferry-md"></a>

## Example Frame: The Last Ferry

New proposed frame for this prototype. Designed for one Leader and three adult players, approximately two hours. It has been reviewed on paper, not playtested. The suggested timing and fictional material are local design choices.

### Purpose and choices

A grounded story about responsibility and competing obligations during a storm. The characters maintain a small island ferry service. Water is rising, the return sailing is overdue, and the harbor authority orders the service closed.

- **Meta: Minimal.** Prepared characters and an immediate opening keep setup short. Players adapt the supplied relationships before starting.
- **Macro: Prepared.** Introduction leads to Planning, then Encounter. New information can return the crew to Planning. Recovery shows who and what their decisions preserved or cost.
- **Micro: 2d6.** Relevant Tags have a noticeable effect on uncertain acts. Natural double 1 is Dire, double 6 Shine; otherwise the modified total is Negative at 6 or below, Trade at 7–9, Positive at 10 or above. Use the fictional judgment about insufficient Tags described in the [Micro reference](#references-micro-md).
- **Tools: None.** Injuries, fatigue, equipment faults, and time pressure are described through the fiction and relevant notebook changes. No hidden Health or countdown system is used.
- **Tag Tree: Open.** Players can propose fitting changes with the Leader's agreement. The supplied notebooks are starting points, not an entry quota.

### Meta opening and ending

Allow about 15 minutes to present the premise and procedures, let players choose and adjust characters, and briefly check tone, boundaries, and readiness. Each player says why the ferry matters to their character. Agree on a shared Focus in the crew's notebook. Introduce the rules for uncertain acts and respect a pause called by anyone. Signal entry into the fiction.

Aim for about 85 minutes in the fiction, leaving about 20 minutes for a fictional landing and an offgame ending. These are pacing estimates, not phase timers. Afterwards, recall a decision that changed the crew's relationship, hear feedback, and review Focus and lasting notebook changes. Do not require consensus about whether their choice was right.

### Local setting

**The terminal:** A waiting room, stores, and a boarding ramp. Several passengers are stranded. The public display reports a cancelled sailing, but a handheld radio still receives the ferry's calls.

**The maintenance shed:** A sheltered place with tools, a portable pump, and charts of the channel. The pump can assist the ferry or clear the terminal's flooded electrical room; it cannot be in both places at once.

**The outer berth:** The ferry waits beyond a damaged navigation light. The crew aboard can manoeuvre, but they cannot see whether debris blocks the approach. Radio contact is patchy, not impossible.

The authority can authorize closure and provide a road vehicle on the mainland. It has no rescue boat immediately available. Establish these facts freely when the characters seek them; they are the situation's basis, not rewards locked behind a roll.

### People and pressures

**Edda, harbor supervisor:** She wants everyone accounted for and the berth closed before conditions worsen. She can arrange shelter in a nearby school and call the mainland crew. She will reconsider the order if offered a credible safer plan. She opposes unannounced risks, not every proposal from the characters.

```text
Edda
#LocalKnowledge
#Firm
+Harbor Radio
=Intention: Account for everyone before the channel becomes impassable.
@Ferry Crew: They know this crossing better than my paperwork does. #Respect #Frustration
```

**Iven, apprentice:** He has discovered the navigation light's damaged cable and wants to repair it alone. He knows the service walkway, has a harness, and will accept company if treated as competent.

```text
Iven
#Craft|Electrical
#EagerToProveHimself
+Safety Harness
=Intention: Get the navigation light working before the ferry approaches.
@Mara: She taught me everything but still checks my work. #Admiration #Resentment
```

Pressures advance when the fiction calls for it: debris reaches the ramp, the electrical room floods, or the ferry must move to remain clear of drifting objects. Give visible warnings before a threat changes available options. Do not advance a secret numerical clock.

### Prepared characters

Players can change names and connections. Keep relevant capabilities and equipment coherent with the work they do.

```text
Mara, mechanic
#Craft|Repairs
#Observant
#Stubborn
+Toolbox
  ±Spanner
  ±Inspection Lamp
@Iven: He thinks checking his work means I distrust him. #Protective
@Neri: She keeps us talking when I want to shout. #Trusted
=Intention: Bring the ferry home without treating Iven like a child.
```

```text
Neri, terminal coordinator
#Social|Negotiation
#Administration
#CalmUnderPressure
+Harbor Radio
@Edda: She trusts facts when I can get her to listen. #ProfessionalRespect
@Sol: He promises passengers more than we can always deliver. #Affection #Impatience
=Intention: Keep the crew and stranded passengers informed and involved.
```

```text
Sol, deckhand
#Move|Swimming
#Seamanship
#Reckless
+Safety Line
+Waterproof Torch
@Mara: She once pulled me out of the channel. #Indebted
@Neri: She is the reason I come back for another season. #Fondness
=Intention: Make sure no one is left waiting without help.
```

The crew can use a shared entry such as `=Intention: Get everyone through the storm.` Ask what this means to each character; they may disagree about whether it requires bringing the ferry into the berth.

### Begin and respond

**Introduction:** The boarding ramp shudders as debris strikes it. Over the radio, the ferry's skipper asks whether the damaged light can guide them in. Edda arrives with the closure order. Ask each character what they are doing.

**Planning:** Make the known facts available: the light's cable fault, the portable pump's competing uses, possible shelter, and the ferry crew's ability to wait or change course. Let the players contact people, inspect the situation, and divide work. Routine communication or inspection succeeds without a roll when failure would add nothing meaningful.

**Encounter:** Focus on the pressure their plan meets. Repairing the exposed cable, guiding the approach, protecting the flooded terminal, or negotiating coordinated help can each be a focused situation. Use ordinary Micro Loops, not a mandatory combat or a single roll for the entire plan. Edda and Iven act from their motives and respond to persuasive reasons or practical assistance.

For example, Mara can attempt to restore the cable while Sol anchors the line. Establish whether the means make success possible, which Tags actually apply, and what failure could mean. A Trade can restore the light while costing the inspection lamp or leaving the access walkway unusable. A Negative can force retreat while revealing a route from the shed; do not erase the next opportunity to act.

**Return to Planning:** Bring new consequences back to the group. A failed approach can lead to sheltering passengers and directing the ferry to a safer anchorage. If they reject Edda's order, she asks how they intend to keep everyone accounted for and may offer support to a credible alternative. If they refuse the repair, Iven can ask for help returning from the walkway rather than becoming an unavoidable casualty.

**Recovery:** Show who reached safety, what remains damaged, and how trust changed. Bringing the ferry in, guiding it elsewhere, or closing the terminal can each give the session a meaningful ending. Let their actions decide the outcome.

Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).

---

<a id="examples-shared-supplies-md"></a>

## Example: A User-Defined Tool

New proposed Tool for this prototype, not a Tool from the book. Its procedure can be supplied in a conversation or a frame document.

### Shared Supplies

Purpose: make the choice between onward travel and replenishment visible during an expedition.

Preparation: the group records a shared Prop with `-Supplies: 3`. Supplies has a range of 0–3 in this example. One player updates it where everyone can see it. The frame uses 1d6 for uncertain acts; Supplies is a separate counter and has no roll of its own.

Procedure:

1. Before a travel stage, the Leader describes what places or distance that stage covers. If Supplies is 0, the group must obtain supplies before beginning another stage.
2. After completing a stage, reduce Supplies by 1, to a minimum of 0. A failed attempt that never completes the stage does not trigger this automatic reduction.
3. The group may consume one extra Supplies for an established practical use, such as feeding stranded travellers. State the cost before the choice; it is not a universal way to buy success on an uncertain act.
4. Obtaining a usable cache or replenishing at a settlement increases Supplies by the amount the Leader establishes from the fiction, to a maximum of 3. Ordinary purchasing succeeds without a roll when neither uncertainty nor meaningful failure applies. When acquisition is uncertain and failure matters, use the selected 1d6 Micro Loop.

These thresholds and restrictions are this Tool's proposed design. Another frame can define Supplies differently.

### Record and use

```text
+Shared Stores: Food and essentials carried by the expedition.
  -Supplies: 3
=Intention: Reach the upland village before the pass closes.
```

After the first completed stage, change the Note to `-Supplies: 2`. Feeding stranded travellers at the stated cost of one changes it to 1. Completing the next stage changes it to 0; the group can remain there, seek help, or replenish, but cannot begin another stage under this Tool until it has supplies.

Suppose the group searches an abandoned shelter for food. The Leader judges the act uncertain and accepts `#Observation`. On an initial 3, the player may keep Trade or reroll once because of the relevant Tag. A reroll of 5 is Positive and must be kept. The Leader establishes that the usable stores replenish Supplies by 1. The Tool does not turn the Tag into +1 or award three units merely because the roll succeeded.

### Adaptation check

If a user supplies only `-Supplies: 3`, the assistant cannot assume this procedure. If they instead define a value reduced every day, follow that trigger rather than converting it to stages. When two active Tools use separate values, keep their triggers, storage, and consequences distinct unless the frame explicitly connects them.

Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).
