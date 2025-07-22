# Tech & AI News Telegram Bot

A lightweight Python automation bot that collects the latest Technology and AI news from various RSS feeds and posts short summaries to a Telegram channel.

Perfect for anyone who wants to keep an audience up to date on AI, tech, startups, and innovation — in English or any other languages.

---

## Features

- Parses and summarizes articles from multiple RSS feeds
- Supports bilingual content (English  or any other languages)
- Filters duplicate articles using a simple hash-based log
- Posts article title, summary, and source link
- Can run via cron (Linux) or Task Scheduler (Windows)

---

## Project Structure

tech-ai-news-bot/
- `tech_ai_news_bot.py` – Main bot script  
- `tech_ai_feeds.txt` – List of RSS feed URLs (one per line)  
- `posted_articles.txt` – Tracks posted articles to prevent duplicates  
- `requirements.txt` – Python dependencies  
- `README.md` – You're reading it!  

---

## Requirements

- Python 3.8+
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- Telegram Channel where the bot is admin

Install dependencies:

pip install -r requirements.txt

---

## How to Use

1. Add your **Telegram bot token** and **channel ID** in `tech_ai_news_bot.py`
2. Edit `tech_ai_feeds.txt` to include RSS sources you trust (one per line)
3. Run the bot manually:

python tech_ai_news_bot.py

4. Or schedule it every 10 minutes using `cron` (Linux):
*/10 * * * * /path/to/venv/bin/python /full/path/to/tech_ai_news_bot.py


(You can use **Task Scheduler** on Windows.)

---

## Example Output

📰 Google's New Gemini AI Update Just Dropped
The latest Gemini model adds multi-modal search and better context windows for coders...
🔗 https://techcrunch.com/google-gemini-update

---

## Future Ideas

- Add inline images or article thumbnails  
- Use ChatGPT to auto-summarize longer articles  
- Cross-post to X, Discord, or Instagram  
- Filter or group by category (AI, Web3, Startups)

---

## License
MIT License — Free to use, modify, and share.

---

## Credits

Created by **Agnostic** as a learning project for Telegram news automation.  
Telegram Channel: [@globaltech_ai](https://t.me/globaltech_ai)
Feel free to **fork**, **star**, or contribute.
