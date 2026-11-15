# Unified Table Language

Source: the book's Word Definitions, pp. 22–24, and UTL chapter, pp. 31–50. See [Sources](sources.md) for edition and editorial distinctions.

## Entries and attachment

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

## Tags and breadth

Use concrete qualities and capabilities that can matter in play. Tags may help, hinder, establish a possibility, or have no mechanical effect in the current situation. The Leader decides which Tags apply under the selected Micro Loop.

Separate levels of breadth with `|`: General, Domain, Niche. For example, `#Craft`, `#Craft|Woodworking`, and `#Craft|Woodworking|Boatbuilding` are three separate choices. A narrower Tag does not require or grant the broader Tags.

Keep notebook Tags concise. Put surrounding background in prose where useful. In a Tag Tree or explanatory collection, descriptions explain the available choices. The book's glossary allows Notes attached to Tags as well as Props, Relations, Focus, and Actions; do not turn a particular example's bare-Tag presentation into a universal prohibition on supporting Notes.

An actual title can be written `#Title|Harbor Warden`. A generic class label is rarely as useful as the abilities, qualities, or position that matter in this frame. A character may have several relevant Tags or very few; their life and role determine the detail.

Some frames explicitly assign values to Tags. Do not use `#Agility +2` as a default character model. A shared numerical attribute system requires its own selected Tool or defined local procedure. The UTL symbol alone never specifies a modifier rule.

## Props, contents, and Notes

Props can be belongings, shared resources, places, equipment, spells, or other assets. Add Tags when the qualities matter and Notes when details or selected Tools need them. Do not catalog every ordinary feature.

Use `±` for a contained Prop and `-` for supporting information. A rope inside a case is a Prop; the case's carrying restriction is a Note. When the rope is recorded separately, change its marker to `+` and preserve its description, Tags, and Notes. Moving it does not duplicate it.

The current book places a nested Prop's Notes on separate indented lines. Older material may keep them on the same line. Read such material without losing attachment; use the current structure for new output.

Books may also record spells or recipes as Notes in existing material. Do not convert every such Note into a Prop automatically. When asked to standardize independent contained Props, use `±` and preserve their information.

Mechanical values are contextual. `-Damage: 2`, `-Protection: 3`, and `-Reduction: 3` do not by themselves select a Tool or guarantee identical mechanics. A Prop can be useful without any numerical values.

## Values, levels, and unknowns

A value in brackets follows the entry's name, for example `+Working [2]` or `+Working [X]`. It may express a cost, level, or another frame-defined value. Its meaning comes from the frame or selected Tool. It is not automatically damage, a spell slot, or an attribute bonus.

Determine X before calculating an effect that depends on it. Follow the entry's definition of what varies. If it supplies no measure, the Leader and player agree on X from the intended effect where the selected procedure allows this. Do not silently make every aspect of an effect scale with X. Keep an explicitly supplied combined value such as `[1 / X]` and obtain its definition when its use matters.

`#?`, `#Magic|?`, and `@?: Someone has been leaving food at my door.` preserve uncertainty. Do not replace the unknown part with invented established knowledge during transcription or review.

## Relations

Relations can concern people, groups, creatures, places, institutions, or other entities with personal meaning. A Relation records what the entity means to the notebook's subject. Two people can record the same entity differently without contradiction.

```text
Arin
@Edda: She always hears me out. #Trusted

Vale
@Edda: She remembers every favor I owe. #Wary
```

Neither Relation gives Arin or Vale a personal `#Trusted` or `#Wary` ability. In the book's example, if Arin trusts Edda, Edda may use that relational trust when interacting with Arin. The Leader may also allow Arin to use it when the fiction makes it relevant. Avoid reversing who trusts whom.

## Focus and change

Focus can belong to a player, character, NPC, or group. Keep an out-of-fiction purpose distinct from a character's intention: a player can explore betrayal through a character devoted to loyalty.

Use labels suited to the intention, such as `=Hope`, `=Question`, `=Task`, or `=Intention`. They are examples, not a closed taxonomy. Resolving a Focus changes `=` to `≠`; retain the entry as history and describe how it ended when that is useful. Resolution includes abandonment or failure, not only success.

Parentheses preserve an unavailable element: `(+Rope)` or `(#Melee)`. A passive Tag contributes no positive roll bonus, though its history may still matter in the fiction. Remove parentheses when the relevant fictional change makes the entry active again. Do not reactivate something merely to improve a roll.

## Actions

Read [Micro Loops](micro.md) before specifying or resolving a rolled Action. A character declaring an act is not automatically using a defined `>Action`.

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

## Shared notebooks

A shared notebook can record group circumstances, assets, Relations, and Focus alongside individual character notebooks. A shared reputation can matter when the group is recognized; it does not automatically give every member the same skills. Access to a shared Prop follows its location and the fiction. A group Relation can differ from an individual's Relation to the same person.

This is an application of the project's working text on a shared group record. It does not establish a new official notebook type, universal party bonus, or required group sheet.

Based on FRAME and Unified Table Language by [Folkin.io](https://folkin.io).
