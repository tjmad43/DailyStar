# Daily Star Tumblr Bot

## Set up venv
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install requests pytumblr beautifulsoup4`

## Scrape Wiki list
- in `populateDB.py`
- use Wiki List of brightest stars since all included have their own page
- (but there is ony 96, maybe update this in future)
- `response = requests.get(URL)` to get HTML of page
- use BeautifulSoup to parse into a Python object tree
- from soup object find the table on page
- find anchor tag to extract name and link
- strip down to page name to be used as `https://en.wikipedia.org" + star_link["href"]`

### Database
- use SQLite database to store star links
- open connection to `stars.db`
- create table
- add list of stars to it
- print out to check
- close connection

## Tumblr authentication
- in `bot.py`
- save tumble consumer & oauth keys and secrets in .env, as well as blog name
- load into python with `dotenv`, `os.getenv()`
- to get tumblr consumer keys:
  - Tumblr API Console: https://www.tumblr.com/oauth/apps
  - _+ Register application_
  - fill in app name, blog URL as Application Website, description
  - default callback URL `http://localhost/callback`
  - `http://localhost http://127.0.0.1` in OAuth2 redirect URLs (placeholder, not needed)
- to get tumblr oauth keys:
  - `pip install requests requests-oauthlib`
  - run `tumblrauth.py`
  - go to URL it prints out and authorise
  - callback URL will not work, but the token and verifier are in the URL it tries to reach
  - take verifier and paste back into script
  - OAuth token and secret will be printed, paste into .env

## Get article info from Wiki API


## Make post


## Keep track of posted stars


## Automate