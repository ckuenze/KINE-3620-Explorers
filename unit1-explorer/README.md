# Unit 1 Explorer

One page with a tab for each Unit 1 lecture in KINE 3620. Signs follow the class coordinate system (+x right, +y anterior, +z superior) and the right-hand rule. Angles are in radians.

| Tab | Lecture | What you can do |
|---|---|---|
| Signs | 1. Planes, Axes, and Our Coordinate System | Pick a joint motion and a side to see its plane, axis, and which direction is positive. A quick-check quiz gives random motions to sign. |
| Linear | 2. Linear Kinematics | Opens the [Kinematics Graph Linker](../kinematics-graph-linker/) on Usain Bolt's 100 m. |
| Angular | 3. Angular Kinematics | Opens the Kinematics Graph Linker on the elbow curl. |
| Force plate | 4–5. Newton's Laws; Center of Mass and GRF | Scrub through a squat and watch COM velocity, COM acceleration, and vGRF = m·(g + a) change together. Adjust body mass, depth, and speed. |
| Torque | 6. Torque, Moment Arms, and Levers | Place an effort and a load on a lever. See the lever class, theoretical mechanical advantage, each torque, the net torque, and the effort needed to balance. |
| Angle of pull | 7. Line of Action and Angle of Pull | Move the elbow and shoulder. See the biceps angle of pull, its rotary and parallel components, the muscle and dumbbell torques, and the force needed to hold still. |

## Pre-class and In-class modes

A switch at the top of the page changes what each tab shows above its tool:

- **Pre-class** (default): guided steps that walk through the tool for that lecture's companion reading ("Before class" list), plus check questions. Click a question to show its answer.
- **In-class**: a partner challenge. Predict first, test it with the tool, then talk through the discussion questions. These come from the activities in each lecture's slides.

The Force plate tab labels its Lecture 4 and Lecture 5 parts. The tools work the same in both modes.

Link straight to a mode and a tab with the query and the hash, for example `index.html?mode=in#torque`. Modes: `pre`, `in`. Tabs: `signs`, `linear`, `angular`, `plate`, `torque`, `pull`. Add `embed=1` (for example `index.html?embed=1&mode=in`) when the page sits inside another page; it hides the mode buttons, so set the mode in the URL.

## Offline file

`unit1-explorer-offline.html` is the whole explorer in one file, with the Kinematics Graph Linker built in. It works when opened straight from a computer (no internet, no other folders), so it is the one to download or share with students. The linked `index.html` needs the `kinematics-graph-linker` folder beside it and a web server (such as GitHub Pages).

`index.html` and `../kinematics-graph-linker/index.html` are the source of truth. After editing either one, rebuild the offline file from the repo root:

```
python unit1-explorer/build_standalone.py
```

## Notes

All curves and values are idealized teaching models, not measurements from real participants. The angle-of-pull tab uses a simplified biceps (origin 0.30 m up the humerus, insertion 0.05 m along the forearm), the same model as the lecture slides. The tool doesn't round θ, so answers can differ from the slides in the last digit.

The Linear and Angular tabs load the Kinematics Graph Linker from this repository, so keep both folders together if you download the linked files.
