import sqlite3
import requests
import random
import pytumblr
import os
from dotenv import load_dotenv

# --- Tumblr auth ---
load_dotenv()

client = pytumblr.TumblrRestClient(
    os.getenv("TUMBLR_CONSUMER_KEY"),
    os.getenv("TUMBLR_CONSUMER_SECRET"),
    os.getenv("TUMBLR_OAUTH_TOKEN"),
    os.getenv("TUMBLR_OAUTH_SECRET")
)

BLOG_NAME = os.getenv("BLOG_NAME")


# --- Get random article ---
def get_random_star():
    conn = sqlite3.connect("stars.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, url FROM stars WHERE posted = 0 ORDER BY RANDOM() LIMIT 1")
    star = cursor.fetchone()

    star_id, star_name, star_url = star

    # Mark as posted
    cursor.execute("UPDATE stars SET posted = 1 WHERE id = ?", (star_id,))
    conn.commit()

    conn.close()
    return star  # (name, url)


# --- Get Wiki API info ---
def get_summary(title):
    api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    headers = {"User-Agent": "DailyStarBot/1.0 (https://github.com/tjmad43/DailyStar)"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return {
            "title": data.get("title"),
            "description": data.get("description"),
            "extract": data.get("extract"),
            "url": data.get("content_urls", {}).get("desktop", {}).get("page"),
            "thumbnail": data.get("thumbnail", {}).get("source"),
        }
    else:
        print(f"Could not fetch {title}, status {response.status_code}")
        return None
    

# --- Make post ---
