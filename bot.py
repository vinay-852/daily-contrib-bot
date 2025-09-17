import os
import requests
import random

DISCORD_WEBHOOK = os.environ["DISCORD_WEBHOOK"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

# Step 1: Fetch candidate issues from GitHub
INTERESTS = ["web", "documentation", "AI", "deep learning"]
# Pick 2 interests randomly for today's batch
today_interests = random.sample(INTERESTS, 2)
QUERY = f'label:good-first-issue state:open ({" OR ".join(today_interests)})'
URL = f"https://api.github.com/search/issues?q={QUERY}&sort=updated&order=desc&per_page=50"

headers = {"Authorization": f"token {GITHUB_TOKEN}"}
resp = requests.get(URL, headers=headers).json()
issues = resp.get("items", [])

if not issues:
    requests.post(DISCORD_WEBHOOK, json={"content": "❌ No issues found today."})
    exit()

# Shuffle to send different issues each day
random.shuffle(issues)
issues = issues[:20]  # top 20 candidates

# Step 2: Ask Gemini to pick the top 5 most promising issues
payload = {
    "contents": [{
        "parts": [{
            "text": f"Here are GitHub issues:\n{issues}\n\nPick the 5 most promising for contribution success. "
                    f"Return as a numbered list with Title and URL only."
        }]
    }]
}

g = requests.post(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent",
    headers={"Content-Type": "application/json"},
    params={"key": GEMINI_API_KEY},
    json=payload
)

gemini_issues = g.json()["candidates"][0]["content"]["parts"][0]["text"]

# Step 3: Send the top issues to Discord
message = f"🔔 **Daily Open Source Contribution Picks** 🔔\n\n{gemini_issues}"
requests.post(DISCORD_WEBHOOK, json={"content": message})
