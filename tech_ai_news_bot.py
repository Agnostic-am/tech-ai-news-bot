import feedparser
import hashlib
from telegram import Bot
import time
import html2text

# === CONFIG ===
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHANNEL_ID = '@YOUR_TELEGRAM_CHANNEL_ID'
FEED_FILE = 'tech_ai_feeds.txt'
POSTED_LOG = 'posted_articles.txt'
MAX_POSTS_PER_RUN = 5  # Limit to 5 posts per run

bot = Bot(token=BOT_TOKEN)

# Load RSS URLs
with open(FEED_FILE, 'r') as f:
    feeds = [line.strip() for line in f if line.strip()]

# Load posted article hashes
try:
    with open(POSTED_LOG, 'r') as f:
        posted = set(line.strip() for line in f)
except FileNotFoundError:
    posted = set()

new_posts = []

# HTML-to-clean-text converter
html_converter = html2text.HTML2Text()
html_converter.ignore_links = False
html_converter.body_width = 0

# Parse feeds
for url in feeds:
    feed = feedparser.parse(url)
    for entry in feed.entries:
        uid = hashlib.md5(entry.link.encode()).hexdigest()
        if uid in posted:
            continue

        title = entry.title.strip()
        link = entry.link.strip()
        summary_raw = entry.summary.strip() if hasattr(entry, 'summary') else ''
        summary = html_converter.handle(summary_raw)

        message = f"🧠 {title}\n\n{summary[:500]}...\n🔗 {link}"
        new_posts.append((uid, message))

        if len(new_posts) >= MAX_POSTS_PER_RUN:
            break
    if len(new_posts) >= MAX_POSTS_PER_RUN:
        break

# Send posts to Telegram
for uid, msg in new_posts:
    try:
        bot.send_message(chat_id=CHANNEL_ID, text=msg)
        print(f"✅ Posted: {uid}")
        posted.add(uid)
        time.sleep(1)
    except Exception as e:
        print(f"❌ Failed to post: {e}")

# Save posted hashes
with open(POSTED_LOG, 'w') as f:
    for uid in posted:
        f.write(f"{uid}\n")
