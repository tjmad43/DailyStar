import sqlite3

# Connect to the database
conn = sqlite3.connect("stars.db")
cursor = conn.cursor()

# Reset all stars to unposted
cursor.execute("UPDATE stars SET posted = 0")
conn.commit()

# Check how many rows were reset
cursor.execute("SELECT COUNT(*) FROM stars WHERE posted = 0")
count = cursor.fetchone()[0]
print(f"Reset {count} stars to unposted.")

conn.close()
