import requests
from bs4 import BeautifulSoup
import sqlite3


# --- Wiki scraping ---
# Get brightest star page
headers = {
    "User-Agent": "DailyStarBot/1.0 (https://github.com/tjmad43/DailyStar; tabbymadhavan@gmail.com)"
}
URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")


# Find the <h2 id="Table">
table_heading = soup.find("h2", {"id": "Table"})
if table_heading is None:
    raise Exception("Could not find the 'Table' heading")

# Find the fourth table after this heading
table = table_heading
for _ in range(4):
    table = table.find_next("table")
    if table is None:
        raise Exception("Could not find correct table after the heading")

# Loop over rows (skip header row)
stars = []
for row in table.find_all("tr")[1:]:
    cells = row.find_all("td")
    if len(cells) > 1:  # avoid blank rows
        star_link = cells[2].find("a")
        if star_link:
            star_name = star_link.text.strip()
            star_url = "https://en.wikipedia.org" + star_link["href"]
            print(star_name, star_url)



# --- Database ---
# Connect to db
conn = sqlite3.connect("stars.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS stars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    posted INTEGER DEFAULT 0
)
""")
conn.commit()

# Insert star data
cursor.executemany("INSERT INTO stars (name, url) VALUES (?, ?)", stars)
conn.commit()

# Check what was added
cursor.execute("SELECT * FROM stars LIMIT 5")
print(cursor.fetchall())

# Close connection
conn.close()