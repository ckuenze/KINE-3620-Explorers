# Reaction Time Lab

Measure your own simple and choice reaction time, see what slows you down, and connect your results to agility on the field or court. A companion scoreboard turns the lab into a class contest.

- **Topic:** Simple vs. choice reaction time, Hick's law, response inhibition, feints and cueing, reactive agility
- **Use:** In-class
- **Unit:** Unit 3: Movement and Human Performance

## Files

| File | Who uses it | What it does |
|---|---|---|
| `index.html` | Students | The Reaction Time Lab: three experiments, results, badges, and agility questions |
| `scoreboard.html` | Instructor | The Reaction Time Classic scoreboard: loads students' results and runs the class contest |

## Learning objectives

After using this tool, students should be able to:

- Define stimulus, reaction time, median, and anticipation, and explain why the median is used.
- Compare reaction time to a light and a sound.
- Describe how reaction time grows as the number of choices increases (Hick's law).
- Explain the cost of a reversed rule, a stop signal, a late change (feint), and a misleading cue.
- Calculate the distance an athlete travels before reacting (speed × reaction time) and relate it to reactive agility testing.

## How to use the lab (students)

Open `index.html` in a web browser. Use a keyboard if you can; a touchscreen or mouse also works.

1. **Experiment 1, Simple.** Respond to a light and to a beep. No headphones? You can skip the sound block.
2. **Experiment 2, Choices.** Respond to 1, 2, 3, or 4 possible boxes.
3. **Experiment 3, Twists.** Opposite side, go or stop, late change, and a hint arrow that is sometimes wrong.
4. Make a prediction before each experiment, then compare it with your results, badges, and the agility questions on the **Results** tab.

For the class contest, type your name on the **Results** tab and click **Save for scoreboard**. Turn in the `RTLAB_Name.txt` file where your instructor tells you.

## How to run the contest (instructor)

Open `scoreboard.html` in a web browser on the computer connected to the projector.

1. **Enter Scores.** Drop in the `RTLAB_Name.txt` files students save from the lab (many at once, including a Canvas submissions download), paste name-and-code lines, or type times by hand.
2. **Rules.** Choose the events that count, track meet scoring (10, 8, 6, 5, 4, 3, 2, 1) or everyone-scores, and the penalty for wrong responses or early presses.
3. **Scoreboard.** Standings with points for each experiment, a leader tile, and a leaders ticker. Click a student to see their event-by-event breakdown. Use the division buttons (Keyboard, Touch, Mouse) for a fair race across devices.
4. **Crown the champion** for the winner screen.
5. **Save for website** downloads a standalone results page you can post. It offers initials only, which is recommended for a public page.

To try it before class, click **Load sample athletes** on the Enter Scores tab (made-up names), then **Clear everything**.

## Privacy

Everything runs in the browser. Nothing is uploaded. The lab clears its results when the page closes unless the student saves them. The scoreboard keeps scores only in the browser on the computer that runs it. No student results are part of this repository.

## Details

- **Files:** `index.html` and `scoreboard.html` (standalone; load Google Fonts)
- **Data:** Students' own responses only. Screens, speakers, and keyboards add delay, so compare conditions within one device rather than across devices.
- **Instructor tab (lab):** Paste class results codes to see class medians and differences.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
