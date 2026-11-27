# Reaction Time Lab

Measure your own simple and choice reaction time, see what slows you down, and connect your results to agility on the field or court. The same page holds the instructor's class scoreboard (the Reaction Time Classic).

- **Topic:** Simple vs. choice reaction time, Hick's law (RT = a + b·log2 n), response inhibition, feints and cueing, reactive agility
- **Use:** Pre-class and in-class (Lecture 17, Agility, Change of Direction, and Reaction Time)
- **Unit:** Unit 3: Movement and Human Performance (Unit 3 Explorer, "L17 Agility" tab)

## One file, three modes

| Link | Who uses it | What it does |
|---|---|---|
| `index.html?mode=pre` (default) | Students, alone, before class | Guided steps: the light block and the 1, 2 and 4 box blocks. Predictions, your Hick's law fit (a and b), and check questions. No headphones, no contest, no name. |
| `index.html?mode=in` | Students, in class | All three experiments, Results, badges, agility questions, and **Save for scoreboard** / results code. |
| `index.html?mode=board` | Instructor only | The Reaction Time Classic scoreboard: load students' results, run the contest, see the class pattern. |

Students see two buttons, **Pre-class** and **In-class**. The scoreboard has no student button. Open it with `?mode=board` or the small "Instructor only" link at the bottom of the lab.

## Learning objectives

After using this tool, students should be able to:

- Define stimulus, reaction time, median, accuracy, and early press (false start), and explain why the median is used.
- Compare reaction time to a light and a sound.
- Describe how reaction time grows as the number of choices increases: by about the same amount each time the number of choices doubles, so by less with each added choice (Hick's law, RT = a + b·log2 n).
- Explain the cost of a reversed rule, a stop signal, a late change (feint), and a misleading cue.
- Calculate the distance an athlete travels before reacting (speed × reaction time) and relate it to reactive agility testing.

## How to use the lab (students)

Use a keyboard if you can: the Space bar for one signal and the number keys 1 to 4 for the boxes. A touchscreen or mouse also works. Press Esc to stop a block.

**Pre-class:** run the light block, then the 1, 2 and 4 box blocks. On **Results**, write down your light median, your 1 box and 4 box medians, and your cost per doubling (b). Answer the check questions. Bring your answers and one question to class.

**In-class:**
1. **Experiment 1, Simple.** Respond to a light and to a beep. No headphones? You can skip the sound block.
2. **Experiment 2, Choices.** Respond to 1, 2, 3, or 4 possible boxes.
3. **Experiment 3, Twists.** Opposite side, go or stop, late change, and a hint arrow that is sometimes wrong.
4. Make a prediction before each experiment, then compare it with your results.

For the class contest, type your name or a nickname on **Results** and click **Save for scoreboard**. Turn in the `RTLAB_Name.txt` file where your instructor tells you. If the download is blocked (some embedded pages), copy the line shown instead.

## How to run the contest (instructor)

Open `index.html?mode=board` on the computer connected to the projector.

1. **Rules.** Announce them before the run. Each event ranks the **adjusted time** = median RT ÷ accuracy (inverse efficiency), so fast guessing does not beat careful responding. Below the accuracy floor (default 80% correct) an athlete gets no points in that event. Sound is off by default (Bluetooth delay). Choose track meet scoring (10, 8, 6, 5, 4, 3, 2, 1) or everyone-scores. An extra per-error penalty is optional (default 0).
2. **Enter Scores.** Drop in the `RTLAB_Name.txt` files (many at once, including a Canvas submissions download), choose them with the file picker, paste name-and-code lines, or type times and % correct by hand.
3. **Scoreboard.** Standings with points per experiment, a leader tile, and a leaders ticker (Pause button; static if the computer asks for reduced motion). Select a name to see the event-by-event breakdown. Use the division buttons (Keys, Touch, Mouse) for a fair race across devices. Initials only is on by default.
4. **Class Pattern.** Class medians, the class Hick's law slope (b), light minus sound, and the other differences. No names.
5. **Crown the champion** for the winner screen (Esc or Close returns).

**Save and back up.** The board saves itself in the browser when it can. If the browser cannot save (private window, embedded page, blocked storage), a red banner says so. Use **Save board (JSON)** for a backup file and **Load board** to restore it on any computer. **Save results (CSV)** keeps each code in column 2, so the CSV can be dropped back in. **Save for website** downloads a standalone results page (initials only by default).

To try it before class, click **Load sample athletes** (made-up names, including "Guessing Gus", who is fast but inaccurate), then **Clear everything**.

## Results code

`RTLAB2|dev=kb|sv=231|...|hi=470|sv_a=100|...|early=2|err=3|ck=NN`: device, 13 median times (ms), % correct per condition, early presses, wrong-or-slow responses, and a checksum (sum of character codes mod 97). A code that fails the checksum is accepted but flagged "may have been edited". Older `RTLAB1` codes still load; they have no accuracy and are flagged in the roster.

## Privacy

Everything runs in the browser. Nothing is uploaded, and the page makes no external requests (system fonts only). The student modes do not read or write browser storage; results vanish when the page closes unless the student saves them. The scoreboard keeps scores only in the browser on the instructor's computer and in files the instructor saves. Projected names default to initials. No student results are part of this repository.

## Details

- **Files:** `index.html` (one standalone file; works from disk and inside the Unit 3 Explorer)
- **Data:** Students' own responses only. Screens, speakers, and keyboards add delay, so compare conditions within one device rather than across devices.
- **Accessibility:** Go and stop are shown with text and shape (GO with a dot; STOP with ✕ and a dashed border), not color alone. Keyboard operable throughout, visible focus outlines, ARIA tabs, live announcements of each reaction time. The visual task cannot be done with a screen reader alone; the sound block with the Space bar is the accessible option.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
