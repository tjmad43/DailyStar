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

    cursor.execute("SELECT name, url FROM stars ORDER BY RANDOM() LIMIT 1")
    star = cursor.fetchone()

    conn.close()
    return star  # (name, url)
