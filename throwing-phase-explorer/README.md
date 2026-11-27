# Throwing Phase Explorer

Step through the six phases of an overhand baseball pitch and a windmill softball pitch, alone or side by side. An animated stick figure, a phase timeline, and illustrative shoulder and elbow curves show where the arm goes, which feet are on the ground, and where the load lands.

- **Topic:** Phases, events, and joint loading in baseball and windmill softball pitching
- **Use:** Pre-class (Lecture 18 reading) and in-class (partner video lab)
- **Unit:** Unit 3: Movement and Human Performance (Unit 3 Explorer tab "L18 Pitching")

## Learning objectives

After using this tool, students should be able to:

- Name the six phases of the baseball pitch (Wind-up, Stride, Arm cocking, Arm acceleration, Arm deceleration, Follow-through) and the event that starts and ends each one (peak knee height, stride foot contact, MER, ball release, maximum internal rotation).
- Name the six phases of the windmill softball pitch using clock positions, and describe where the ball is released.
- Identify the base of support (single or double) in each phase.
- Explain why the external valgus moment on the elbow is greatest near the end of arm cocking, and which tissues supply the internal varus torque that resists it.
- Explain why arm acceleration is so brief, and estimate an average angular velocity in rad/s from video frames.
- Describe the kinetic chain sequence from stride to wrist flexion.
- Explain why the softball pitch is not "easy on the arm."

## How to use it

Open `index.html` in a web browser.

- Pick **Pre-class** or **In-class** at the top (or add `?mode=pre` / `?mode=in` to the URL; the default is pre).
  - **Pre-class:** guided steps that match the Lecture 18 reading (step through the phases, find release with Hand path, read MER in rad, compare softball release), short check questions, then the Quick check.
  - **In-class:** partner video-lab prompts (predict, match your video frames to the phases, discuss) and a frames-to-ω calculator (Δt = frames ÷ frame rate; ω_avg = Δθ ÷ Δt, in rad/s with °/s in parentheses).
- Choose **Baseball pitch**, **Windmill softball pitch**, or **Side-by-side**.
- Press **Play**, pick a speed (0.25x, 0.5x, 1x), or drag the slider to scrub through the delivery. Phase timing is scaled for viewing; in a real pitch, arm acceleration lasts about 0.03 s.
- Use a phase chip (or **Prev/Next phase**) to jump to a phase. The colored timeline bar can also be clicked.
- Turn on **Hand path** to see the full path of the throwing hand.
- Read the phase card for the purpose, key actions, base of support, start and end events, and where the load is.
- Answer the six **Quick check** questions.

## Conventions

- Angles in rad with degrees in parentheses, e.g., MER about 3.05–3.14 rad (175–180°); shoulder internal rotation velocity about 122 rad/s (7,000°/s).
- Shoulder: external rotation is positive, measured as rotation of the arm relative to the trunk (includes scapular and trunk motion). This is the convention used across Lectures 18–19. Some figures in class plot internal rotation as positive; the tool says so under the chart.
- Elbow: external valgus moment vs. internal varus torque (UCL plus flexor–pronator muscles). Torques plotted are internal joint torques.
- Time: 0% = first movement, 100% = end of follow-through. Ball release is at 89% (baseball) and 86% (softball).

## Details

- **File:** `index.html` (standalone; loads Google Fonts, falls back to system fonts offline)
- **Data:** Poses and curve shapes are illustrative teaching models, not motion-capture data from a specific athlete. Labeled reference values come from Dillman 1993, Fleisig 1995, Fleisig 1996, MacWilliams 1998, Barrentine 1998, Maffet 1997, and Werner 2005 (full citations with DOIs are in the tool).
- **Links:** `?mode=pre|in`, `?embed=1` (hides the mode buttons and posts the page height to a parent page), and `?sport=softball&t=80` (or `sport=both`, `trail=1`) to open a specific moment.
- **Accessibility:** keyboard-operable buttons with `aria-pressed`, visible focus rings, a live phase readout, figure and chart text alternatives that update, contrast at or above WCAG 2.1 AA, and reduced-motion support.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
