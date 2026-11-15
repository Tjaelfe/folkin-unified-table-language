# Tools and Frame Context

Source: pp. 276–277 and 341–343. Tools are optional procedures or aids selected for a frame. The book's examples are not a closed list.

## Read an existing or user-defined Tool

Use the supplied description even when the Tool is unfamiliar. Find the information the task needs: its purpose, preparation, trigger, who handles it, what changes, what the change means, and its connections to UTL, other Tools, or the selected Micro Loop. A Tool need not have numbers or dice.

Do not require a registry, configuration file, or software integration. Context may be in the conversation or an ordinary frame document. Ask for a missing procedural detail only when the current result depends on it. A note such as `-Supplies: 3` alone does not define a consumption rule.

Distinguish a **counter die**, which displays a changing value, from **resolution dice**, which are rolled for an uncertain act. Health 1d6 may be a counter in a frame that resolves acts with 2d8. A Tool mentioning its own explicit roll is not automatically translated to another Micro Loop: check the actual procedure and identify any proposed adaptation.

This prototype includes the Health procedure below. Other book Tools are not fully documented in this package. If asked to use one whose procedure is not supplied, obtain the relevant description instead of inventing its exact rules. A proposed new Tool must be clearly identified as new.

## Build or adapt a Tool

Identify the activity, condition, or decision that needs support. First consider whether existing Tags or a selected procedure already serve it. Define the preparation, trigger, handler, changes, effects, and connections. Keep the amount of handling proportional to its purpose.

Try ordinary use, an edge state, and recovery or reset where relevant. Check compatibility with the chosen Micro Loop and other active Tools. Provide an example that shows what changes in the fiction. The [Shared Supplies example](../examples/shared-supplies.md) demonstrates a complete new procedure with no registry or additional dice system.

## Health 1d6

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
