# Daily Star Tumblr Bot

DailyStar is a Python project that scrapes Wikipedia’s [List of brightest stars](https://en.wikipedia.org/wiki/List_of_brightest_stars) and posts one star per day to Tumblr. Each post includes the star’s name, summary, and a link back to Wikipedia, with optional photo thumbnails.
View at https://dailystarreport.tumblr.com

---

## Features
- Scrapes the brightest stars from Wikipedia
- Stores stars in a local SQLite database with `posted` tracking
- Uses the Wikipedia API to fetch star summaries and images
- Posts daily to Tumblr via the Tumblr API
- Supports tags, bold text, and line breaks in posts
- Can be scheduled with `cron` (Linux/macOS) or Task Scheduler (Windows), or with Tumblr queue

---

## Tech Stack
- **Python 3**
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) (HTML parsing)
- [SQLite](https://www.sqlite.org/) (database for star tracking)
- [Requests](https://docs.python-requests.org/) (HTTP requests)
- [pytumblr](https://github.com/tumblr/pytumblr) (Tumblr API client)
- [requests-oauthlib](https://requests-oauthlib.readthedocs.io/) (OAuth flow)
