"""Build ONE self-contained Unit 3 Explorer (works offline when downloaded) from the individual tools.
Usage: python unit3-explorer/build_standalone.py [OUT]   (default: unit3-explorer/unit3-explorer-offline.html)
Source of truth: each tool's <folder>/index.html plus unit3-explorer/index.html (the iframe-based shell).
Each tool is stored inside the page and loaded into its tab's iframe with srcdoc; the mode/view query that a
tool normally reads from location.search is injected as window.__U2Q instead."""
import io, os, re, json, sys

T = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(T)  # repo root (this script lives in unit3-explorer/)
TPL = os.path.join(T, "index.html")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(T, "unit3-explorer-offline.html")
FOLDERS = ["countermovement-jump-explorer", "reaction-time-lab", "throwing-phase-explorer", "launch-angle-challenge"]

page = io.open(TPL, encoding="utf-8").read()
tools = {}
for f in FOLDERS:
    h = io.open(os.path.join(R, f, "index.html"), encoding="utf-8").read()
    n = h.count("new URLSearchParams(location.search)")
    assert n >= 1, f
    h = h.replace("new URLSearchParams(location.search)", "new URLSearchParams(window.__U2Q || location.search)")
    assert re.search(r"<head[^>]*>", h, re.I), f
    tools[f] = h
blob = json.dumps(tools, ensure_ascii=False).replace("</", "<\\/")

old_fns = ("function toolUrl(t, mode) { return `../${t.folder}/index.html?mode=${mode}${t.extra}&embed=1`; }\n"
           "function soloUrl(t, mode) { return `../${t.folder}/index.html?mode=${mode}${t.extra}`; }")
new_fns = ("const U2TOOLS = JSON.parse(document.getElementById('u2tools').textContent);\n"
           "function toolQ(t, mode, embed) { return `?mode=${mode}${t.extra}${embed ? '&embed=1' : ''}`; }\n"
           "function toolDoc(t, q) { return U2TOOLS[t.folder].replace(/<head([^>]*)>/i, m => m + '<script>window.__U2Q=' + JSON.stringify(q) + ';<\\/script>'); }\n"
           "let soloBlob = null;")
old_load = ("  const url = toolUrl(t, st.mode);\n")
new_load = ("  const url = t.folder + toolQ(t, st.mode, true);\n")
old_src = "  if (st.fr.getAttribute('src') !== url) st.fr.setAttribute('src', url);   // reloads the tool with the new mode\n"
new_src = "  if (st.fr.dataset.q !== url) { st.fr.dataset.q = url; st.fr.srcdoc = toolDoc(t, toolQ(t, st.mode, true)); }   // reloads the tool with the new mode\n"
old_solo = "  st.solo.innerHTML = `<a href=\"${soloUrl(t, st.mode)}\" target=\"_blank\" rel=\"noopener\">Open ${t.title} in its own window</a>`;\n"
new_solo = ("  if (soloBlob) URL.revokeObjectURL(soloBlob);\n"
            "  soloBlob = URL.createObjectURL(new Blob([toolDoc(t, toolQ(t, st.mode, false))], { type: 'text/html' }));\n"
            "  st.solo.innerHTML = `<a href=\"${soloBlob}\" target=\"_blank\" rel=\"noopener\">Open ${t.title} in its own window</a>`;\n")
for a, b in [(old_fns, new_fns), (old_load, new_load), (old_src, new_src), (old_solo, new_solo)]:
    assert a in page, a[:60]
    page = page.replace(a, b)
page = page.replace("</body>", f'<script type="application/json" id="u2tools">{blob}</script>\n</body>', 1)
# the data block must come before the main script that parses it: move the main script after it
i_data = page.index('<script type="application/json" id="u2tools">'); i_main = page.index("<script>\nconst TABS")
if i_main < i_data:
    end_main = page.index("</script>", i_main) + len("</script>")
    main = page[i_main:end_main]; page = page[:i_main] + page[end_main:]
    page = page.replace("</body>", main + "\n</body>", 1)
page = page.replace("Each tool also works on its own: use the “Open it in its own window” link.",
                    "This one file contains every Unit 3 tool and works offline. Each tool can also open in its own window.")
io.open(OUT, "w", encoding="utf-8", newline="").write(page)
print("wrote", OUT, round(len(page.encode("utf-8")) / 1024), "KB,", len(tools), "tools")
