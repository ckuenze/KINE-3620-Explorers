# Unit 2 Explorer

One page for all of Unit 2, with one tab per lecture. Each tab embeds the matching tool and has its own Pre-class / In-class switch.

- **Topic:** Unit 2 lectures 8–14 (muscle, balance, gait cycle, gait kinematics, moments, running, sprinting)
- **Use:** Pre-class and in-class (mode switch on each tab; `?mode=pre` or `?mode=in` sets the starting mode)
- **Unit:** Unit 2: Introduction to Human Movement

## Tabs

| Tab | Tool(s) |
|---|---|
| L8 Muscle | `muscle-architecture-explorer` |
| L9 Balance | `balance-external-moment-arm` |
| L10 Gait cycle | `walking-gait-phase-explorer`, `walking-gait-vgrf-explorer`, `gait-cycle-video-analyzer` (sub-switch) |
| L11 Gait kinematics | `gait-cycle-video-analyzer` (joint-angle view, `?view=angles`) |
| L12 Moments | `moment-arm-explorer` (elbow moment arms, plus Window 3 "Knee and the GRF") |
| L13 Running | `running-gait-cycle-explorer` |
| L14 Sprinting | `sprinting-kinetics-explorer` |

## How to use it

There are two versions:

- **`unit2-explorer-offline.html` (one download, works offline):** every Unit 2 tool is packed into this single file. Download it and open it in a browser. No other files or internet connection are needed (fonts fall back to the system font offline). This is the version to post on a course site.
- **`index.html` (linked version):** loads each tool from its folder in this repo. It works online, or from disk when the tool folders sit next to it.

After editing any tool, rebuild the offline file from the repo root with `python unit2-explorer/build_standalone.py`.

- Pick a lecture tab. Arrow keys move between tabs.
- Pick **Pre-class** or **In-class**. The tool reloads in that mode.
- **Deep links:** `#l8` … `#l14`, plus `#l10-vgrf` and `#l10-video` for the L10 sub-tools. For example, `index.html?mode=in#l12` opens Moments in in-class mode.
- Each tab links to its tool in its own window.

## Details

- **Files:** `index.html` (linked shell; loads Google Fonts), `unit2-explorer-offline.html` (built, self-contained), `build_standalone.py` (builds the offline file). Tools load on a tab's first open, with `?mode=pre|in&embed=1`.
- State passes only through the iframe URL. Embedded tools post their page height so each frame fits.
- **Data:** Idealized models for learning; not patient data.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
