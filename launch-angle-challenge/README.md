# Launch Angle Challenge

How release speed, release angle, and release height decide where a thrown ball goes. Before class, students explore the range-versus-angle curve on their own. In class, tables play a 5-round game. **Long toss** is about throwing for distance. **Hit the target** is about accuracy: get the ball to a glove, base, or bucket before the runner arrives.

- **Topic:** Projectile motion in throwing: release speed, angle, and height
- **Use:** Pre-class (Lecture 19 reading) and in-class (team game)
- **Unit:** Unit 3: Movement and Human Performance (Unit 3 Explorer tab "L19 Release")

## Learning objectives

After using this tool, students should be able to:

- Explain why 0.79 rad (45°) gives the longest throw only when release and landing heights are equal and there is no air drag.
- Explain why a release height above the ground lowers the best release angle.
- Describe why release speed matters more than fine-tuning angle (range grows with speed squared, and the range curve is flat near its peak).
- Explain how a speed–angle tradeoff (athletes throw slower when they aim higher) and air drag push the best angle lower still.
- Identify the two angles that reach a target (a line drive and a lob) and explain why the flatter throw arrives sooner.

## How to use it

Open `index.html` in a web browser.

- Pick **Pre-class** or **In-class** at the top (or add `?mode=pre` / `?mode=in` to the URL; the default is pre).
  - **Pre-class (single player):** the team game is hidden and **The physics** card opens with guided steps that match the Lecture 19 reading. It starts at v = 13 m/s and h = 2.1 m. Students move **Your release angle** to find the longest throw, then set h = 0, then turn on Real athlete. Expected answers: 0.73 rad (41.9°), 19.21 m; 0.79 rad (45°), 17.23 m; 0.63 rad (36.2°), 18.79 m.
  - **In-class (team game):** "Before you throw, predict" prompts from the Lecture 19 slide, then the 5-round game.
- Type a **Team name**, pick a game type (**Long toss** or **Hit the target**) and a sport (baseball, softball, javelin-ish, shot put).
- Optional: turn on **Real athlete** (Long toss only) and **Air drag** (baseball only).
- Leave **Same conditions for every team** on so every table gets the same five rounds.
- Set the release angle (and speed in Hit the target), then press **Throw!** After each throw the tool shows the best angle and distance for that round, or both angles that hit the target and their flight times.
- Changing game type or sport mid-game asks "Leave this game?" with inline **Yes, leave** / **No, keep playing** buttons (no pop-up dialogs, so it works inside a sandboxed Canvas iframe).
- After round 5, project the **Final results** screen and work through the **What did you learn?** prompts. **Full screen** appears only when the browser allows it (an iframe needs `allow="fullscreen"`).

## Speed–angle model (Real athlete)

The tool uses the same linear model as the Lecture 19 slide (range vs. release angle with a speed–angle tradeoff):

v(θ) = v₃₅ − k·(θ − 0.61 rad)

v₃₅ is the release speed at 0.61 rad (35°), and k is in m/s per rad. The slide's example is the shot-put case: v₃₅ = 13 m/s, k = 2.29 m/s per rad (0.04 m/s per degree), h = 2.1 m, best angle 0.63 rad (36.2°) at 18.79 m. The presets use k = 5.73 m/s per rad (0.10 per degree) for baseball and javelin-ish, 5.16 (0.09) for softball, and 2.29 (0.04) for shot put. All k values are illustrative, not measurements. The idea comes from Linthorne NP. Optimum release angle in the shot put. *J Sports Sci* 2001;19:359–72. doi:10.1080/02640410152006135.

(Earlier versions used speed = top speed − k × angle measured from 0°, with k in m/s per degree. That model was changed so the tool and the slide give the same numbers.)

## Details

- **File:** `index.html` (standalone; loads Google Fonts, falls back to system fonts offline)
- **Angles:** shown in rad first with degrees in parentheses; sliders move in 0.01 rad steps. Physics code works internally in degrees and converts for display.
- **Data:** Trajectories use drag-free projectile equations, or an approximate quadratic drag model for a baseball (0.145 kg, 7.4 cm, Cd about 0.35; RK4 integration) when Air drag is on. A built-in self-test (browser console) checks the formulas against brute force and the slide model. Sport presets are generic teaching values, not records or measurements.
- **Links:** `?mode=pre|in`; `?embed=1` hides the mode buttons and posts the page height to a parent page.
- **Storage:** Personal bests and the team name are saved only in this browser, if it allows local storage. Nothing is uploaded.
- **Accessibility:** labeled sliders with `aria-valuetext`, toggle buttons with `aria-pressed`, canvases with `role="img"` and labels that update after each throw, visible focus rings, contrast at or above WCAG 2.1 AA, and reduced-motion support.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
