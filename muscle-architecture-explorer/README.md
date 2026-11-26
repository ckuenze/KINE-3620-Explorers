# Muscle Architecture Explorer

A small tool for two architecture ideas from the muscle lecture. Pennation angle sets how much of a fiber's force reaches the tendon (F·cos α). Fascicle length sets how fast the fascicle can shorten when its sarcomeres shorten at the same rate.

- **Topic:** Pennation angle, tendon force, fascicle length and shortening velocity
- **Use:** Pre-class and in-class (mode switch; `?mode=pre` or `?mode=in`)
- **Unit:** Unit 2: Introduction to Human Movement (Lecture 8)

## Learning objectives

After using this tool, students should be able to:

- Calculate the force along the tendon from fiber force and pennation angle: F·cos α, with α in radians.
- Explain why a more pennate muscle can still produce more force (more fibers in parallel, higher PCSA).
- Explain why a longer fascicle (more sarcomeres in series) shortens faster for the same sarcomere shortening rate.
- Connect F·cos α to the parallel component from angle of pull (Lecture 7), with α measured from the tendon line.

## How to use it

Open `index.html` in a web browser.

- Pick **Pre-class** or **In-class** at the top. Pre-class shows guided steps and check questions. In-class shows a partner challenge and discussion questions, and adds the fascicle B length slider and the F·sin α readout. The **Lost to angle** readout, (1 − cos α) × 100, shows in both modes.
- **Window 1:** move the pennation angle α (0 to 0.70 rad) and the fiber force. The calculation shows cos α, then F·cos α.
- **Window 2:** set the sarcomere shortening rate and press **Play** to watch both fascicles shorten over 0.25 s (slow motion). Fascicle A = 0.10 m (fixed) and fascicle B = 0.05 m (In-class: B adjustable, 0.04–0.15 m), matching the Lecture 8 deck. The calculation shows v = L × rate for each.
- `?embed=1` hides the tool's own mode buttons (used by the Unit 2 Explorer).

## Accessibility

Labeled sliders with spoken units, diagrams with text descriptions that update, a polite live region for results, visible focus outlines, WCAG AA colors, and a Play button that respects reduced-motion settings.

## Details

- **File:** `index.html` (standalone; loads Google Fonts)
- **Data:** Idealized models for learning, not measurements from a specific muscle.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
