# Running Gait Cycle Explorer

Compare walking and running in two ways: how the gait cycle is structured (double support vs. float phase), and how the vertical ground reaction force (vGRF) curve changes shape, including the impact peak seen with a rearfoot strike.

- **Topic:** Walking vs. running mechanics (Lecture 13)
- **Use:** Pre-class and in-class (mode switch at the top; open with `?mode=pre` or `?mode=in`)
- **Unit:** Unit 2: Introduction to Human Movement

## Learning objectives

After using this tool, students should be able to:

- State that a float (flight) phase is the one mechanical feature that defines running.
- Explain why walking has double support and running has a float phase instead.
- Describe how stance shrinks (as % of the cycle and in seconds) as running pace increases.
- Compare walking vGRF (peaks just above 1 BW) with running vGRF (about 2.0–2.5 BW at a jog, higher with speed).
- Identify the impact peak, the active (second) peak near midstance, and loading rate (BW/s) on a running vGRF curve.
- Explain why comparing curves by % of stance differs from comparing them in real time.

## How to use it

Open `index.html` in a web browser.

- **Pre-class mode:** guided steps and check questions for the reading's "Before class" list. Controls: running pace, curve toggles, the x-axis switch (% of stance vs. time), and the stance scrubber.
- **In-class mode:** partner predict-then-test challenges and discussion questions (same controls).
- Use the **Running pace** slider. It changes both the gait-cycle bars and the running vGRF curves.
- Toggle each curve (walking, forefoot, rearfoot) on and off. The rearfoot curve is hidden at Sprint pace.
- Press **Impact peak**, **Active (second) peak**, or **Loading rate** to highlight that feature. Loading rate = first vGRF peak ÷ time to that peak (BW/s), the same definition as the decks: the impact peak for rearfoot, the active peak for forefoot (no impact peak), the first peak for walking. The equation shown reproduces the result.
- `?embed=1` hides the tool's own mode buttons (used by the Unit 2 Explorer).

## Details

- **File:** `index.html` (standalone; loads Google Fonts)
- **Conventions:** walking phases use the Unit 2 scheme (loading response 0–10%, midstance 10–30%, terminal stance 30–50%, pre-swing 50–60%, swing 60–100%). Values to 2 decimals.
- **Data:** Stance percentages and vGRF curves are illustrative models of typical patterns, not data from a specific runner.
- **Accessibility:** labeled controls with spoken values, toggle state on buttons, text summaries of the bars and chart, line patterns in addition to color, visible focus.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
