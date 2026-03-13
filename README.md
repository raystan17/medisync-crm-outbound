# Outbound Engine

Lightweight outbound messaging system for MediSync Labs investor outreach.

## Workspace (password protected)

Open the **workspace** to view investors, LinkedIn DMs, templates, and generated output in one place.

**Local:** Double-click `workspace/serve.bat` or run `npx serve -p 8080` from the project folder, then open http://localhost:8080

**Deploy:** See [DEPLOY.md](DEPLOY.md) to push to GitHub and deploy on Vercel.

**Password:** pillow123 (for you and Brock)

## Generate messages

```bash
pip install -r requirements.txt
python scripts/generate_messages.py
```
