# Moment Arm Explorer

Use the elbow as a model to see how a single joint angle changes both the internal (muscle) and external (forearm weight) moment arms, and why torque changes across the range of motion even when force stays the same. Window 3, **Knee and the GRF**, applies τ = F × d⊥ to the ground reaction force at the knee (Lecture 12).

- **Topic:** Moment arms and torque vs. joint angle
- **Use:** Pre-class and in-class (mode switch; `?mode=pre` or `?mode=in`)
- **Unit:** Unit 2: Introduction to Human Movement (Lecture 12)

## Learning objectives

After using this tool, students should be able to:

- State τ = F × d⊥ and its units (N·m).
- Define the moment arm as the perpendicular distance from the joint center to a force's line of action.
- Explain why the external (weight) moment arm follows d = L × sin θ, and why the muscle moment arm changes with angle.
- Tell internal from external moments and give their signs at the elbow (flexion +).
- Use the sign of the net moment to say which way the forearm angularly accelerates.
- Find the external knee moment from the GRF (M = F × d⊥) and its sign (knee extension +: GRF in front = external extension moment +, behind = external flexion moment −), and the equal and opposite internal moment needed.

## How to use it

Open `index.html` in a web browser. Choose a mode at the top:

- **Pre-class:** guided steps and check questions tied to the reading's "Before class" list.
- **In-class:** a predict-then-test partner challenge, discussion questions, and a "force to hold" readout (net moment = 0).

Controls: **elbow flexion angle** (radians, degrees in parentheses; 0 rad = hanging straight down, 2.62 rad = curled up), **muscle force**, and **forearm + hand weight**. Both forces are the same at every angle.

**Window 3 (Knee and the GRF):** sliders for GRF magnitude (0–3000 N), GRF angle from the ground (1.05–2.09 rad, measured from the ground ahead, +y; degrees in parentheses) and the GRF line's perpendicular distance from the knee (0–0.15 m), plus a side toggle (in front of / behind the knee). A to-scale sagittal schematic shows the shank, thigh, knee, COP and GRF arrow. The calculation shows the components (F_y = F·cos φ, F_z = F·sin φ), M_ext = ±F × d⊥ and M_int = −M_ext, all to 2 decimals in N·m, plus a verdict naming the muscle group. Quasi-static: segment weight and inertia are ignored. Pre-class and In-class each have Window 3 steps.

- **Window 1** shows each moment arm (in metres, 3 decimals) against angle.
- **Window 2** shows internal (solid) and external (dashed) torque size against angle, the signed calculation, and the net moment.

Add `&embed=1` to hide the mode buttons when the page is embedded (the Unit 2 Explorer does this).

## Details

- **File:** `index.html` (standalone; loads Google Fonts)
- **Model:** The muscle moment-arm curve is an illustrative pattern (smallest at the ends of the range, largest near 1.57 rad), not a measured curve for a specific muscle. Forearm center of mass 0.20 m from the elbow.
- **Accessibility:** labeled sliders with spoken units, updating text descriptions of each chart, a polite live summary, dashed vs. solid lines with direct labels, visible focus outlines, and WCAG AA contrast.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
