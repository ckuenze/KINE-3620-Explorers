# Gait Cycle Video Analyzer

Load a sagittal-plane (side) walking video, and in class a frontal-plane video too. Step through them frame by frame, mark gait events, read step and stride timing, and measure joint angles right on the image with our sign convention.

- **Topic:** 2D video analysis of walking gait (gait cycle events, timing, and joint angles)
- **Use:** Pre-class and in-class (mode switch; `?mode=pre` or `?mode=in`)
- **Unit:** Unit 2: Introduction to Human Movement (Lecture 10 gait cycle, Lecture 11 gait kinematics)

## Learning objectives

After using this tool, students should be able to:

- Identify initial contact, opposite toe off, heel off, opposite initial contact, and toe off on video, and place them in the gait cycle phases.
- Compute stride time, stance time, stance %, step time, and cadence (steps/min) from marked events.
- Measure a joint angle from three points (proximal, joint center, distal) and report it in radians with our signs: hip flexion +, knee flexion − (extension +), ankle dorsiflexion +.
- Explain why each joint center is an estimate, and how moving one point changes the angle.
- Measure step width as side-to-side distance (|Δx|), in metres once a scale is set.
- Explain the limits of 2D video: frame rate, camera angle, and scale.

## How to use it

Open `index.html` in a web browser.

1. Pick **Pre-class** (side view only, guided steps and check questions) or **In-class** (both views, sync, step width, partner challenge).
2. **Choose video**. Phone videos work; MP4 (H.264) is the most reliable format.
3. Enter the clip's **frame rate** (phone slow motion is often 120 or 240 fps), then use **◂ Frame / Frame ▸**.
4. Set **Subject walks** (left → right or right → left). This sets which way is anterior, so it sets the angle signs.
5. *(Optional)* **Trim** to one or two gait cycles. Frame stepping stays inside the trim.
6. **Events & timing:** choose the limb, then mark events. The timing box fills in as soon as the needed events exist.
7. **Joint angles:** pick a joint and place three points by clicking, or with the keyboard (Tab to the video, arrow keys move a crosshair, Shift for bigger steps, Enter to place, Escape to cancel), or by typing x/y pixel values.

URL options: `?mode=pre|in`, `?view=events|angles` (opens on that section; `angles` preselects the knee), `&embed=1` (hides the mode buttons when embedded in the Unit 2 Explorer).

## Privacy

Videos stay in your browser for this session only. Nothing is uploaded or saved, so reloading the page clears everything. Write down your measurements before you leave the page.

## Details

- **File:** `index.html` (standalone; loads Google Fonts)
- **Angles:** each angle is shown as our signed joint angle and as the included angle, in radians (2 decimals) with degrees in parentheses. Knee = included − 180° (negative when flexed); hip = thigh relative to the trunk line, + when the thigh is ahead; ankle = 90° − included angle between shank and foot. The canvas y axis points down, so the tool flips it before computing signs. The front view reports included angles only.
- **Gait phases:** initial contact 0%, loading response 0–10%, midstance 10–30%, terminal stance (heel off) 30–50%, pre-swing (push off) 50–60%, toe off 60%, initial swing 60–73%, mid swing 73–87%, terminal swing 87–100%.
- **Accessibility:** all controls are labeled and keyboard-operable, toggles expose `aria-pressed`, status messages are announced, and points can be placed without a mouse.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
