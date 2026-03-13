# Outbound Engine

Lightweight outbound messaging system for MediSync Labs investor outreach.

## Workspace

Open the **workspace** to view investors, LinkedIn DMs, templates, and generated output in one place.

**Option 1 — Double-click:** Run `workspace/serve.bat` (Windows)

**Option 2 — Terminal:**
```bash
cd outbound-engine
python -m http.server 8080
```
Then open **http://localhost:8080/workspace/** in your browser.

## Generate messages

```bash
pip install -r requirements.txt
python scripts/generate_messages.py
```
