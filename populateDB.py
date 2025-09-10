import requests
from bs4 import BeautifulSoup
import sqlite3


# --- Wiki scraping ---
# Get brightest star page
headers = {
    "User-Agent": "DailyStarBot/1.0 (https://github.com/tjmad43; tabbymadhavan@gmail.com)"
}
URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")


tables = soup.find_all("table")

print(f"Found {len(tables)} tables on the page.")
for i, t in enumerate(tables):
    classes = t.get("class")
    print(i, classes)


# # Find table on page
# table = soup.find("table", {"class": "wikitable sortable"})

# if not table:
#     raise Exception("Could not find the table on the page. Wikipedia structure may have changed.")

# # Loop over rows (skip header row)
# for row in table.find_all("tr")[1:]:
#     cells = row.find_all("td")
#     if len(cells) > 1:  # avoid blank rows
#         star_link = cells[1].find("a")
#         if star_link:
#             star_name = star_link.text.strip()
#             star_url = "https://en.wikipedia.org" + star_link["href"]
#             print(star_name, star_url)



# # --- Database ---
# # Connect to db
# conn = sqlite3.connect("stars.db")
# cursor = conn.cursor()

# # Create table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS stars (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     url TEXT NOT NULL
# )
# """)
# conn.commit()

# # Insert star data
# cursor.executemany("INSERT INTO stars (name, url) VALUES (?, ?)", stars)
# conn.commit()

# # Check what was added
# cursor.execute("SELECT * FROM stars LIMIT 5")
# print(cursor.fetchall())

# # Close connection
# conn.close()