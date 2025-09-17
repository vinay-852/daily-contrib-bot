
import os
import requests

DISCORD_WEBHOOK = os.environ["DISCORD_WEBHOOK"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

# Search for good issues
QUERY = "label:good-first-issue state:open (web OR documentation OR AI OR deep-learning)"
URL = f"https://api.github.com/search/issues?q={QUERY}&sort=updated&order=desc&per_page=30"

headers = {"Authorization": f"token {GITHUB_TOKEN}"}
resp = requests.get(URL, headers=headers).json()
issues = resp.get("items", [])[:20]  # fetch up to 20 issues

if not issues:
    requests.post(DISCORD_WEBHOOK, json={"content": "❌ No issues found today."})
    exit()

# Ask Gemini to filter down to 10
payload = {
    "contents": [{
        "parts": [{
            "text": f"Here are GitHub issues:\n{issues}\n\nPick the 10 most promising issues for contribution success. Return as a simple list with title and URL."
        }]
    }]
}

g = requests.post(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent",
    headers={"Content-Type": "application/json"},
    params={"key": GEMINI_API_KEY},
    json=payload
)

gemini_text = g.json()["candidates"][0]["content"]["parts"][0]["text"]

# Send to Discord
message = f"🔔 **Daily Open Source Contribution Picks** 🔔\n\n{gemini_text}"
requests.post(DISCORD_WEBHOOK, json={"content": message})
