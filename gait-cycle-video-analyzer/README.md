# Gait Cycle Video Analyzer

Load a frontal-plane and a sagittal-plane walking video, step through them frame by frame, mark gait events, time steps and strides, and measure joint angles right on the image.

- **Topic:** 2D video analysis of walking gait
- **Use:** In-class
- **Unit / week:** [UNIT]

## Learning objectives

After using this tool, students should be able to:

- Identify initial contact, midstance, toe-off, and mid-swing on video.
- Measure step and stride time from video.
- Measure a joint angle with the proximal / joint center / distal method.
- Compare step width between steps in the frontal plane.
- Explain the limits of 2D video analysis, including frame rate, camera angle, and lack of real-world scale.

## How to use it

Open `index.html` in a web browser.

1. **Choose video** for the frontal and sagittal views. Phone videos work. MP4 (H.264) is the most reliable format.
2. Set the **fps** to match the video's frame rate, then use **◂ Frame / Frame ▸** to step.
3. *(Optional)* **Trim** to one or two gait cycles. This only narrows playback and doesn't edit the file.
4. *(Optional)* **Sync** the two views: scrub each one to the same event, then click **Set sync point here**.
5. Choose the limb (**R / L**), then mark events, steps, and strides.
6. To measure an angle, pick a joint and click three points: proximal, joint center, then distal.

## Privacy

Videos stay in your browser for this session only. Nothing is uploaded or saved, so reloading the page clears everything. Write down your measurements before you leave the page.

## Details

- **File:** `index.html` (standalone; loads Google Fonts)
- **Step width** is reported in pixels only, because the video has no real-world scale.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
