# Unit 3 Explorer

One page for all of Unit 3, with one tab per lecture. Each tab embeds the matching tool and has its own Pre-class / In-class switch.

- **Topic:** Unit 3 lectures 15–19 (countermovement jump, jump landing, agility and reaction time, pitching, release)
- **Use:** Pre-class and in-class (mode switch on each tab; `?mode=pre` or `?mode=in` sets the starting mode)
- **Unit:** Unit 3: Movement and Human Performance

## Tabs

| Tab | Tool |
|---|---|
| L15 Jump | `countermovement-jump-explorer` (jump view) |
| L16 Landing | `countermovement-jump-explorer` (landing view, `?view=landing`) |
| L17 Agility | `reaction-time-lab` |
| L18 Pitching | `throwing-phase-explorer` |
| L19 Release | `launch-angle-challenge` |

## How to use it

There are two versions:

- **`unit3-explorer-offline.html` (one download, works offline):** every Unit 3 tool is packed into this single file. Download it and open it in a browser. No other files or internet connection are needed. This is the version to post on a course site.
- **`index.html` (linked version):** loads each tool from its folder in this repo. It works online, or from disk when the tool folders sit next to it.

After editing any tool, rebuild the offline file from the repo root with `python unit3-explorer/build_standalone.py`.

- Pick a lecture tab. Arrow keys move between tabs.
- Pick **Pre-class** or **In-class**. The tool reloads in that mode.
- **Deep links:** `#l15` … `#l19`. For example, `index.html?mode=in#l17` opens the Reaction Time Lab in in-class mode.
- Each tab links to its tool in its own window.
- The Reaction Time Lab's instructor scoreboard is not a tab. Open `reaction-time-lab/index.html?mode=board` on the instructor computer.

## Details

- **Files:** `index.html` (linked shell), `unit3-explorer-offline.html` (built, self-contained), `build_standalone.py` (builds the offline file). Tools load on a tab's first open, with `?mode=pre|in&embed=1`.
- State passes only through the iframe URL. Embedded tools post their page height so each frame fits.
- **Data:** Idealized models and example data for learning; not patient data.
- **Author:** Christopher Kuenze, PhD, ATC, FNATA
- **Last updated:** November 2026
