# Sprinting Kinetics Explorer

Three linked windows for sprint kinetics: how force, velocity, power, and momentum relate across a modeled 100 m or 200 m sprint; how the net impulse of one ground contact changes momentum; and how leg stiffness changes contact time, peak force, leg compression, and vertical stiffness.

- **Topic:** Sprinting kinetics (Lecture 14)
- **Use:** Pre-class and in-class (mode switch at the top; open with `?mode=pre` or `?mode=in`)
- **Unit:** Unit 2: Introduction to Human Movement

## Learning objectives

After using this tool, students should be able to:

- State the equations and units for momentum (p = m·v, kg·m/s), power (P = F·v, W), and impulse (J = F·Δt, N·s).
- Explain the impulse–momentum theorem: net impulse = change in momentum.
- Describe how net horizontal force, velocity, and power change across the sprint phases (drive, transition, maximum velocity, speed maintenance).
- Show that braking larger than propulsion gives a negative net impulse and slows the sprinter.
- Describe leg stiffness (k_leg = F_peak ÷ ΔL) during loading and unloading, and how vertical stiffness (k_vert = F_peak ÷ Δy) differs.

## How to use it

Open `index.html` in a web browser.

- **Pre-class mode:** guided steps and check questions for the reading's "Before class" list. Uses the 100 m race. The stiffness presets are available in both modes.
- **In-class mode:** partner predict-then-test challenges and discussion questions. Adds the 200 m race.
- **Window 1:** set sprinter mass and drag **Time in race**. Each equation shows the numbers that produce the readout.
- **Window 2:** set the average net horizontal force (−300 to +600 N), contact time, and entering velocity for one step.
- **Window 3:** set leg stiffness (10–30 kN/m) and read contact time, peak vGRF, ΔL, Δy, and k_vert. Presets: **Lower stiffness (12 kN/m)** and **Higher stiffness (28 kN/m)**.
- `?embed=1` hides the tool's own mode buttons (used by the Unit 2 Explorer).

## Details

- **File:** `index.html` (standalone; loads Google Fonts)
- **Conventions:** step = one contact; speed = step length × step frequency. +y is anterior (running direction). Values to 2 decimals.
- **Data:** Illustrative models (exponential rise to about 11.3 m/s with a smooth late fade; air drag 0.25·v² N; sine-shaped contact force; 700 N sprinter in Window 3), not timing-gate or force-plate data from a real athlete.
- **Accessibility:** labeled controls with spoken values, chart descriptions that update, a polite live summary, phase names in text, visible focus.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
