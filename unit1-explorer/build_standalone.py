"""Build ONE self-contained Unit 1 Explorer that works offline (from file://, no sibling folders).
Usage: python unit1-explorer/build_standalone.py [OUT]   (default: unit1-explorer/unit1-explorer-offline.html)
Source of truth: unit1-explorer/index.html and kinematics-graph-linker/index.html. Edit those, then rerun this.
The graph linker is stored inside the page and loaded into the L2/L3 iframes with srcdoc. The ?scen= query the
linker normally reads from location.search is injected as window.__U1Q instead, and "Open it in its own window"
opens a blob: copy of the linker with the same query."""
import io, os, json, sys

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root (this script lives in unit1-explorer/)
SRC = os.path.join(T, "unit1-explorer", "index.html")
LINKER = os.path.join(T, "kinematics-graph-linker", "index.html")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(T, "unit1-explorer", "unit1-explorer-offline.html")

page = io.open(SRC, encoding="utf-8").read()
linker = io.open(LINKER, encoding="utf-8").read()

# 1. The linker reads its scenario from window.__U1Q when it is embedded.
n = linker.count("new URLSearchParams(location.search)")
assert n == 1, f"expected one location.search reader in the linker, found {n}"
linker = linker.replace("new URLSearchParams(location.search)", "new URLSearchParams(window.__U1Q || location.search)")
blob = json.dumps(linker, ensure_ascii=False).replace("</", "<\\/")

# 2. Swap the frame loader for the srcdoc version (the block is marked in index.html).
old = "function loadFrame(fr) { fr.src = fr.dataset.src; }\n"
new = ("const U1LINKER = JSON.parse(document.getElementById('u1linker').textContent);\n"
       "function linkerDoc(q) { return U1LINKER.replace(/<head([^>]*)>/i, m => m + '<script>window.__U1Q=' + JSON.stringify(q) + ';<\\/script>'); }\n"
       "function loadFrame(fr) { fr.srcdoc = linkerDoc('?' + (fr.dataset.src.split('?')[1] || '')); }\n"
       "document.querySelectorAll('a[data-solo]').forEach(a => {   // 'Open it in its own window' -> a blob: copy of the linker\n"
       "  a.href = URL.createObjectURL(new Blob([linkerDoc(a.dataset.solo)], { type: 'text/html' }));\n"
       "});\n")
assert page.count(old) == 1, "loadFrame block not found in index.html"
page = page.replace(old, new)

# 3. Put the linker data before the main script, which parses it at startup.
main = "<script>\nconst $ = id"
assert page.count(main) == 1, "main script start not found"
page = page.replace(main, f'<script type="application/json" id="u1linker">{blob}</script>\n' + main)

# 4. Footer note.
footer = '<p class="note">KINE 3620 · Unit 1. Idealized models for learning; not patient data.</p>'
assert footer in page
page = page.replace(footer, '<p class="note">KINE 3620 · Unit 1. Idealized models for learning; not patient data. '
                    'This one file contains the whole explorer, including the Kinematics Graph Linker, and works offline.</p>')

io.open(OUT, "w", encoding="utf-8", newline="").write(page)
print("wrote", OUT, round(len(page.encode("utf-8")) / 1024), "KB")
