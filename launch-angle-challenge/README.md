# Launch Angle Challenge

A 5-round class game about how release speed, release angle, and release height decide where a thrown ball goes. **Long toss** is about throwing for distance. **Hit the target** is about accuracy: get the ball to a glove, base, or bucket before the runner arrives. Tables compete by team name.

- **Topic:** Projectile motion in throwing: release speed, angle, and height
- **Use:** In-class
- **Unit:** Unit 3: Movement and Human Performance

## Learning objectives

After using this tool, students should be able to:

- Explain why 45° gives the longest throw only when release and landing heights are equal and there is no air drag.
- Explain why a release height above the ground lowers the best release angle.
- Describe why release speed matters more than fine-tuning angle (range grows with speed squared, and the range curve is flat near its peak).
- Explain how a speed–angle tradeoff (athletes throw slower when they aim higher) and air drag push the best angle lower still.
- Identify the two angles that reach a target (a line drive and a lob) and explain why the flatter throw arrives sooner.

## How to use it

Open `index.html` in a web browser.

- Type a **Team name**, pick a mode (**Long toss** or **Hit the target**) and a sport (baseball, softball, javelin-ish, shot put).
- Optional: turn on **Real athlete** (Long toss only: release speed falls as release angle rises) and **Air drag** (baseball only).
- Leave **Same conditions for every team** on so every table gets the same five rounds.
- Set the release angle (and speed in Hit the target), then press **Throw!** After each throw the tool shows the best angle and distance for that round, or both angles that hit the target and their flight times.
- After round 5, project the big **Final results** screen and work through the **What did you learn?** prompts.
- Open **The physics** for the equations and a live chart of range vs. release angle, with 45° and the best angle marked.

## Details

- **File:** `index.html` (standalone; loads Google Fonts)
- **Data:** Trajectories use drag-free projectile equations, or an approximate quadratic drag model for a baseball (RK4 integration) when Air drag is on. The Real athlete speed–angle tradeoff (speed = top speed − k × angle) is an illustrative model based on the idea in Linthorne NP. Optimum release angle in the shot put. *J Sports Sci* 2001;19:359–72. doi:10.1080/02640410152006135. Sport presets are generic teaching values, not records or measurements.
- **Storage:** Personal bests and the team name are saved only in this browser, if it allows local storage. Nothing is uploaded.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
