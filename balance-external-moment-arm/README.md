# Balance and the External Moment Arm

Change how high the center of mass (COM) sits and how far the body leans forward, and see what happens to the moment arm and to the external moment gravity creates about the ankle. A fixed toe edge shows when the COM line leaves the base of support.

- **Topic:** Balance, COM height, and the external moment from gravity
- **Use:** Pre-class and in-class (mode switch; `?mode=pre` or `?mode=in`)
- **Unit:** Unit 2: Introduction to Human Movement (Lecture 9)

## Learning objectives

After using this tool, students should be able to:

- Calculate the perpendicular moment arm of body weight as d = h × sin θ (θ in radians).
- Calculate W = m·g and the external moment τx = −W·d for a forward lean (right-hand rule about +x, +y anterior).
- Explain why a taller posture creates a larger external moment than a crouched one at the same lean.
- Explain why an ankle strategy runs out once the COM line passes the toe edge, and when a hip strategy or a step is needed.

## How to use it

Open `index.html` in a web browser. Choose a mode at the top:

- **Pre-class:** guided steps and check questions. Controls: **COM height (h)**, **forward lean (θ)** (steps of 0.005 rad; shown as rad with whole degrees in parentheses), and two presets (mass fixed at 70 kg).
- **In-class:** a predict-then-test partner challenge and discussion questions. Adds **body mass** and the *Near the toe edge* and *Past the toe edge* presets.

The **Live calculation** panel shows each step (d, W, τx) with the numbers that reproduce the result, and the internal ankle moment needed to hold still: forward lean gives an external moment of −W·d about x, and the plantar flexors supply an equal and opposite internal moment (no "+" sign is put on it). Add `&embed=1` to hide the mode buttons when the page is embedded (the Unit 2 Explorer does this).

## Details

- **File:** `index.html` (standalone; loads Google Fonts)
- **Model:** A single-segment inverted pendulum pivoting at the ankle, with a fixed toe edge 0.20 m ahead of the ankle. COM height range 0.40–1.10 m. Typical COM height and limits of stability are approximate values, not measured data.
- **Accessibility:** labeled sliders with spoken units, a text description of the diagram, a polite live summary, visible focus outlines, and WCAG AA contrast.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
