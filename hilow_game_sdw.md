<!-- To see this file in a clean, formatted view, select ▼ in the upper-right corner of the editor pane, then select "Markdown Preview". -->

# Software Development Worksheet (SDW)

* **Course:** IT 140 - *Introduction to Scripting*
* **Activity:** Module Four Assignment
* **Program:** Higher/Lower Game

> Use this worksheet as optional working notes while you move through the **Analyze** and **Design** phases of the simplified Software Development Life Cycle (SDLC).
>
> Your notes do not need to be formal or polished. Keep answers brief and write them in your own words. The purpose of the SDW is to help you understand the requirements and plan your own graded pseudocode.
>
> Look for **TODO** prompts. Replace them with your own answers if you use this worksheet.
>
> **This worksheet is not a graded deliverable.** Do not submit it in D2L Brightspace unless your instructor specifically asks for it.

## How to Use This Worksheet

The worksheet uses the same pattern throughout:

* **Where to look** tells you where to find the information you need.
* **Prompt** tells you what to think about or answer.
* Your response goes immediately after the prompt.

The worksheet intentionally asks questions instead of supplying the completed Higher/Lower Game algorithm. Your graded `design/hilow_game.pseudo` should contain **your** design.

# Analyze Phase

## 1. Describe the Problem

**Where to look:** Module Four Assignment Guidelines and Rubric → Overview, Scenario, and Prompt.

**Prompt:** In one or two sentences, describe what the program needs to accomplish for Maria and Bella.

**Your notes:**

The program asks a player to select a range, chooses a random number
within that range, and gives higher/lower feedback until the player guesses
it correctly.

## 2. Identify Inputs and Outputs

**Where to look:** Guidelines and Rubric → Prompt; Higher/Lower Game Sample Output; SRS FR-1, FR-5, and FR-9.

**Prompt:** What information must come from the player, and what categories of information must the program communicate?

**Inputs:**

* Lower bound and upper bound.
* A guess after the range is established.

**Outputs:**

* Prompts for bounds and guesses.
* Validation messages and too-low, too-high, or success feedback.

Do not choose exact message wording yet unless it helps you reason about the behavior.

## 3. Identify Validation Requirements

**Where to look:** Guidelines and Rubric → Prompt; SRS FR-2, FR-3, FR-6, and FR-7.

**Prompt:** Describe each input-validation rule in plain language and what should happen when the rule is not satisfied.

**Your notes:**

* The lower bound must be less than the upper bound. When it is not, display
  a message and obtain both bounds again.
* A guess must be within the selected lower and upper bounds. When it is
  outside the range, reject it and obtain another guess.

## 4. Identify Processing and Decisions

**Where to look:** Guidelines and Rubric → Prompt; SRS FR-4, FR-8, and FR-9.

**Prompt:** What value must the program generate, and what possible relationships between a valid guess and that value must the design distinguish?

**Your notes:**

* A random target number between the valid lower and upper bounds.
* Too low, too high, or equal to the target number.

## 5. Identify Repeated Behavior

**Where to look:** Guidelines and Rubric → Prompt; SRS FR-3, FR-7, FR-10, and FR-11.

**Prompt:** What work can repeat? For each repeated part, what condition causes repetition and what condition lets the program continue or stop?

**Your notes:**

* If bounds are invalid, request both bounds again until the lower bound is
  less than the upper bound.
* If a guess is outside the range, obtain another guess until it is valid.
* Compare each valid guess with the target; continue after too-low or too-high
  feedback and stop when the guess is correct.

## 6. Distinguish Requirements From Extra Features

**Where to look:** SRS → Out of Scope Unless Your Instructor Adds a Requirement.

**Prompt:** List one or two features you might be tempted to add that are not required by the assignment.

**Your notes:**

* A fixed maximum number of guesses.
* Guess counting or a score.

## 7. Analyze Checkpoint

Before moving to Design:

* [ ] I can explain the game's purpose in my own words.
* [ ] I identified the required player inputs.
* [ ] I identified the required categories of output.
* [ ] I can explain both validation requirements.
* [ ] I know when the random number is generated.
* [ ] I can explain the too-low, too-high, and correct outcomes.
* [ ] I can identify the repeated behaviors and their stopping conditions.
* [ ] I did not turn optional features into assignment requirements.

# Design Phase

## 8. Plan the Major Stages

**Where to look:** Your Analyze notes, SRS, and `design/hilow_game_sdd.md`.

**Prompt:** List the major stages of the game in order without writing the completed pseudocode here.

**Your notes:**

1. Obtain and validate the lower and upper bounds.
2. Generate a random target number in the valid range.
3. Obtain a guess and validate it against the range.
4. Compare the guess with the target and provide feedback.
5. Repeat the guessing process until the target is guessed.

## 9. Plan Validation Before Detailed Pseudocode

**Where to look:** Your Analyze notes and SDD → Validation and Decision Branching.

**Prompt:** For each validation requirement, explain what information is checked and how the program can eventually receive acceptable input.

**Your notes:**

* Check that the lower bound is less than the upper bound. If not, repeat
  bound input until the relationship is satisfied.
* Check that each guess is at least the lower bound and at most the upper
  bound. If not, repeat guess input until it is valid.

## 10. Plan Repetition

**Where to look:** Your Analyze notes and SDD → Repetition and Stopping Conditions.

For each repeated section, answer:

* What condition is checked?
* What happens during one repetition?
* What information can change?
* What stops the repetition?

**Your notes:**

Use a bounds-validation loop before random-number generation. Use a
guess-validation loop for every guess. Use a game loop to continue after
incorrect valid guesses. The bounds and guess loops stop after acceptable
input is received, while the game loop stops after the target is guessed.

## 11. Plan Decision Branching

**Where to look:** SRS FR-8 and FR-9.

**Prompt:** What outcomes must the valid-guess comparison distinguish, and what should happen after each outcome?

**Your notes:**

If a valid guess is too low, display feedback and continue. If it is too
high, display feedback and continue. If it equals the target, display success
and stop.

## 12. Requirements-to-Design Traceability

After drafting `design/hilow_game.pseudo`, locate where your design addresses each requirement group.

| Requirement group | Where it appears in your pseudocode |
| --- | --- |
| Bounds input and validation | Establishing and validating the guessing range |
| Random-number generation | Target-number generation after valid bounds |
| Guess input and validation | Guess input and the guess range-validation loop |
| Too-low / too-high / correct decisions | Valid-guess comparison branches |
| Repetition until correct | Outer repeated guessing loop |
| Required outputs | Input prompts and feedback/output statements |

If a required behavior has no corresponding design step, revise the pseudocode.

## 13. Trace a Behavior by Hand

**Where to look:** SRS → Behavior Verification Cases and the official Sample Output.

Choose one scenario that includes repetition or validation. Follow your pseudocode one statement at a time.

**Scenario:** A guess below the selected range

**Trace notes:**

The outer guessing section obtains the guess. The guess-validation loop
rejects it because it is below the lower bound, outputs validation feedback,
and obtains another guess. Only an in-range guess proceeds to comparison.

## 14. Rubric Review

### Logical Steps — 35%

* [ ] My design logically outlines the complete required program.
* [ ] Another programmer could follow the order of the steps.
* [ ] I represented all required functionality.

### Input/Output — 30%

* [ ] I represented both bound inputs.
* [ ] I represented guess input.
* [ ] I represented required feedback and success output.

### Program Flow — 35%

* [ ] I used decision branching for the valid-guess outcomes.
* [ ] I used loops for required repeated behavior.
* [ ] Each loop has an understandable stopping condition.
* [ ] Indentation shows which statements belong inside branches and loops.

## 15. Design Checkpoint

* [ ] Valid bounds are established before the target number is generated.
* [ ] Invalid bounds can lead to new bound input.
* [ ] A guess is validated against the selected range.
* [ ] An invalid guess can lead to another guess.
* [ ] Too-low and too-high valid guesses allow play to continue.
* [ ] A correct guess ends the guessing process.
* [ ] No starter `TODO:` prompts remain in the graded pseudocode.

## 16. Ready to Submit

Before submission:

* [ ] I reviewed the current Module Four Assignment Guidelines and Rubric.
* [ ] I reviewed the official Higher/Lower Game Sample Output.
* [ ] I traced multiple required behaviors through my pseudocode.
* [ ] I saved the graded file as `design/hilow_game.pseudo`.
* [ ] I understand that only the `.pseudo` file is required for submission.

# Optional Construct and Test Notes

Complete the remaining sections only if you choose the optional Python practice after your graded pseudocode is ready.

## 17. Construct Notes — Optional

Open [`src/README.md`](src/README.md) and translate **your own completed pseudocode** into `src/hilow_game.py`.

| Design idea | Python concept you used |
| --- | --- |
| User input | TODO |
| Bounds validation | TODO |
| Random number | TODO |
| Guess validation | TODO |
| Decision branching | TODO |
| Repetition | TODO |
| Output | TODO |

## 18. Test Notes — Optional

Open [`tests/README.md`](tests/README.md).

| Scenario | Expected behavior | Actual behavior | Pass? |
| --- | --- | --- | :---: |
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |

If testing exposes a design problem, revise the graded pseudocode first and then update the optional Python implementation.
