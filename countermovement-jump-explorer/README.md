# Countermovement Jump Explorer

Explore how vertical ground reaction force and center-of-mass (COM) position, velocity, and acceleration change through one countermovement jump and its landing. You can also measure your own jump height, and how fast you stop on landing, from a video.

- **Topic:** CMJ kinetics, the impulse–momentum theorem, work, jump height, and landing (loading rate, stopping distance)
- **Use:** Pre-class and in-class (Lecture 15: Jumping and the Countermovement Jump; Lecture 16: Biomechanics of Jump Landing)
- **Unit:** Unit 3: Movement and Human Performance

## Learning objectives

After using this tool, students should be able to:

- Name the CMJ phases (quiet stance, unweighting, braking, propulsion, flight, landing) and find them on force and COM traces.
- Relate vGRF to COM acceleration with a = (vGRF − BW) ÷ m.
- Use the impulse–momentum theorem (J_net = Δp = m × Δv) to explain where takeoff velocity comes from, and show that net work and net impulse give the same takeoff velocity.
- Tell net work on the COM apart from work by the ground force alone and work by gravity.
- Calculate jump height with the takeoff velocity method (v² ÷ 2g) and the flight time method (g × t² ÷ 8), and explain when the two disagree.
- Calculate contact velocity, loading rate, stopping time and distance, and average vGRF (by impulse and by work) for a landing.

## How to use it

Open `index.html` in a web browser. Two controls sit at the top.

**Pre-class / In-class.** Pre-class shows guided steps and check questions that match the companion reading's "Before class" list. In-class shows partner prompts (predict, then test).

**View: Jump | Landing | Measure from video.**
- **Jump (Lecture 15).** Use the slider, **Play**, or the **Jump to** buttons to move through the jump. Switch between **Time series** and **Force vs. position**, and between **N** and **BW**. Tables show the phases, impulse by phase, a jump summary, and work three ways (net, ground force, gravity). *(Optional)* load a side-view video and mark four events to sync it with the charts.
- **Landing (Lecture 16).** The charts zoom in on the landing (time zero = initial contact). A table lists the example's landing numbers with their equations. The **Drop-landing model** (labeled "model, not data") has sliders for drop height, stopping distance, and mass.
- **Measure from video.** Load a video of your jump, set the frame rates, and mark **takeoff**, **landing (initial contact)** and, optionally, the **lowest point** after landing. You get flight time, jump height with its likely error (both marks), and a landing estimate (stop time, stopping distance, average vGRF in BW). *(Optional)* set a scale and click your COM in each airborne frame to compare takeoff velocity estimates.

**URL options:** `?mode=pre` or `?mode=in`; `?view=jump`, `?view=landing` or `?view=measure`; `?embed=1` hides the mode buttons and reports the page height to a parent page (for the Unit 3 Explorer).

## Privacy

Videos stay on your device. Nothing is uploaded or saved.

## Details

- **File:** `index.html` (standalone; loads Google Fonts and falls back to Arial offline; supports dark mode; works from file:// and inside an iframe)
- **Sign convention:** up is +z.
- **Data:** The example jump is a simulated, representative jump for a 75 kg athlete sampled at 500 Hz. It is not real athlete data. The drop-landing model is a simple steady-slowing model, not data.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
