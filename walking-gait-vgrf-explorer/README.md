# Walking Gait vGRF Explorer

Explore the vertical ground reaction force (vGRF) curve across one stance phase of walking, and see how it changes with walking speed.

- **Topic:** Ground reaction forces in walking
- **Use:** Pre-class and in-class (mode switch; `?mode=pre` or `?mode=in`)
- **Unit:** Unit 2: Introduction to Human Movement (Lecture 10)

## Learning objectives

After using this tool, students should be able to:

- Identify the key features of the walking vGRF curve: stance duration, first peak (load acceptance), second peak (late stance), and loading rate.
- Explain when vGRF is above, equal to, and below body weight using vGRF = m(g + a_COM).
- Describe how faster walking raises both peaks, deepens the midstance dip, and shortens stance time.
- Explain why the anterior–posterior GRF is braking (−y) in early stance and propulsive (+y) in late stance.
- Recognize single and double support when both limbs' vGRF curves are shown together.

## How to use it

Open `index.html` in a web browser. Pick a mode at the top.

- **Pre-class:** speed buttons, the stance slider, and features A–D, BW/N units and body mass, with guided steps and check questions. The body-mass slider works in BW mode too: the curve stays in BW, and the readout shows the N conversion (1.0 BW = m × 9.81 m/s²).
- **In-class:** adds the both-feet panel, the AP GRF panel, predict-then-test challenges, and discussion prompts.
- Choose **Slow / Normal / Fast**. The readout shows % stance, vGRF, and stance time (s).
- Press a feature (**A–D**) to highlight it. D shows the average loading rate (BW/s or N/s) from initial contact to the found B peak.
- Add `&embed=1` to the URL to hide the tool's own mode buttons (used by the Unit 2 Explorer).

## Details

- **File:** `index.html` (standalone; loads Google Fonts)
- **Data:** Curves are illustrative models of typical shapes, not force-plate data. Peaks are about 1.05, 1.17 and 1.29 BW and the midstance dip about 0.76, 0.69 and 0.62 BW (Slow, Normal, Fast). Stance times (0.80, 0.68, 0.58 s) are example values. The AP braking-to-propulsive switch is fixed at 50% of stance.
- **Phases:** stance sub-phases follow the shared Unit 2 scheme (loading response, midstance, terminal stance, pre-swing), shown in % of stance.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
