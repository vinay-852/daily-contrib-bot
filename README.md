# daily-contrib-bot

## Overview
**daily-contrib-bot** is a Python bot that helps open source contributors by curating a daily list of promising GitHub issues and sending them to a Discord channel. It uses the Gemini AI model to filter and select the top issues most likely to lead to successful contributions.

## Features
- Fetches up to 20 recent "good first issues" from GitHub with relevant labels (web, documentation, AI, deep-learning).
- Uses Gemini AI to select the 10 most promising issues for new contributors.
- Posts the curated list to a Discord channel via webhook.
- Automates daily notifications to boost contributor engagement.

## How It Works
1. The bot queries GitHub for open issues labeled "good first issue".
2. Issues are filtered for relevance (web, documentation, AI, deep-learning).
3. Gemini AI processes the list and returns the top 10 picks.
4. The results are posted to your Discord channel.

## Setup Instructions

### Prerequisites
- Python 3.x
- GitHub account and token
- Gemini API key (from Google Generative Language API)
- Discord webhook URL

### Environment Variables
Set the following environment variables in your runtime:
- `DISCORD_WEBHOOK`: Discord webhook URL to post messages.
- `GITHUB_TOKEN`: GitHub personal access token.
- `GEMINI_API_KEY`: Gemini API key for content generation.

### Installation
```bash
git clone https://github.com/vinay-852/daily-contrib-bot.git
cd daily-contrib-bot
pip install -r requirements.txt
```

### Usage
Run the bot with:
```bash
python bot.py
```
Make sure your environment variables are set before running.

## Customization
- Modify the `QUERY` in `bot.py` to adjust labels or topics.
- Tune Gemini prompts for different selection criteria.

## License
This project currently does not specify a license.

## Author
- [vinay-852](https://github.com/vinay-852)

## Contributing
Feel free to open issues or submit pull requests to improve the bot!
