# Kinematics Graph Linker

Scrub one time cursor across three stacked, time-aligned graphs (position, velocity, acceleration, or angle, angular velocity, angular acceleration) and see that the slope of each graph is the value of the graph below it. A small animation shows the motion itself, and a secant tool compares average and instantaneous rates.

- **Topic:** Linear and angular kinematics: slopes, tangents, and average vs. instantaneous rates
- **Use:** Pre-class
- **Unit:** Unit 1: Linear and Angular Kinematics

## Learning objectives

After using this tool, students should be able to:

- Explain that velocity is the slope of the position–time graph and acceleration is the slope of the velocity–time graph (and the same for θ, ω, and α).
- Read the signs of velocity and acceleration at a point and say whether the object is speeding up, slowing down, or momentarily at rest.
- Explain how something can slow down while still moving forward (positive velocity, negative acceleration).
- Calculate an average velocity (Δx/Δt) or average angular velocity (Δθ/Δt) and tell it apart from the instantaneous value.

## How to use it

Open `index.html` in a web browser.

- Choose **Bolt 100 m (real data)**, **Elbow curl**, or **Build your own**.
- Press **Play**, drag the time slider, or click and drag on any graph to move the cursor.
- With **Tangent lines** on, read the slope printed under the top two graphs and compare it with the value on the graph below.
- Turn on **Average (secant)** and drag the purple **t₁** and **t₂** handles on the top graph (or use the sliders) to see the average rate.
- For Bolt, turn on **Segment averages** to see his average velocity over each 20 m.
- In **Build your own**, set x₀, v₀, and a, or pick **Speeding up** or **Slowing down, still moving forward**.
- For the curl, switch angle units between radians and degrees.
- Read the **Read the graph** box, then answer the four **Quick check** questions.

## Details

- **File:** `index.html` (standalone; loads Google Fonts)
- **Data:** Bolt scenario uses the official cumulative 20 m splits and 0.146 s reaction time from the 9.58 s world record (Berlin, 16 August 2009), as reported by *Track & Field News* (November 2009) from the official biomechanical analysis. The curve is a smooth-start sprint model fitted to the split times: with t′ = t − 0.146 s, v = vmax(1 − e^(−t′/τ1))(1 − e^(−t′/τ2))², vmax = 12.2046 m/s, τ1 = 1.1970 s, τ2 = 0.18 s. It reaches every split within 0.02 s (residuals +0.013, −0.007, −0.017, +0.017, −0.003 s at 20–100 m). Acceleration and its slope both start at 0, so the curve leaves zero smoothly, and acceleration peaks at about 9.9 m/s² near 0.47 s. Velocity and acceleration are model estimates, and the model leaves out the small slowdown over the last 20 m that the official segment averages show. The curl (minimum-jerk) and constant-acceleration scenarios are idealized models.
- **Self-test:** Open the browser console to see a built-in check of the model fit to the splits, its smoothness, the official segment averages, and the curl and constant-acceleration equations.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
