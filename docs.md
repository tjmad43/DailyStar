# Daily Star Tumblr Bot

- [Daily Star Tumblr Bot](#daily-star-tumblr-bot)
  - [Set up venv](#set-up-venv)
  - [Scrape Wiki list](#scrape-wiki-list)
    - [Database](#database)
  - [Tumblr authentication](#tumblr-authentication)
  - [Get star from database](#get-star-from-database)
  - [Get article info from Wiki API](#get-article-info-from-wiki-api)
  - [Make post](#make-post)
  - [Automate](#automate)
  - [Reset DB](#reset-db)


## Set up venv
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install requests pytumblr beautifulsoup4`

## Scrape Wiki list
- in `populateDB.py`
- set user-agent header so wiki doesn't reject
- use Wiki List of brightest stars since all included have their own page
- (but there is ony 96, maybe update this in future)
- `response = requests.get(URL)` to get HTML of page
- use BeautifulSoup to parse into a Python object tree
- from soup object find the table on page
  - under Table heading
  - fourth table after that
  - note: improve way of finding this in future
- find anchor tag to extract name and link
- strip down to page name to be used as `https://en.wikipedia.org" + star_link["href"]`

### Database
- use SQLite database to store star links
- open connection to `stars.db`
- create table
  - with a "posted" column to see if a star has been done already
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

## Get star from database
- see `get_random_star()`
- open db connection
- select star that hasn't been posted already (posted=0)
- mark that star as posted now
- close conection and return star

## Get article info from Wiki API
- see `get_summary(title)`
- call `https://en.wikipedia.org/api/rest_v1/page/summary/{TITLE}` to get JSON response with page info
- needs header like previously
- get title, description, extract, url and thumbnail for star

## Make post
- pytumblr docs: https://github.com/tumblr/pytumblr
- photo post with main photo of page, a title, summary, and link to the page
- pages may possibly not have thumbnail so if not, make text post with same structure but no photo
- `state="published"` posts straight away, can queue or save as draft instead
- tags: list of strings

## Automate
to post automatically once a day:
- `state="queue"`
- go to queue on tumblr settings to choose how frequently and when to post
- run `bot.py` however many times to fill up queue
**or** run bot once a day with a cron job:
- in terminal: 
- `crontab -e`
- `0 11 * * * /Users/tabmad/opt/anaconda3/bin/python3 /Users/tabmad/DailyStar/bot.py >> /Users/tabmad/DailyStar/bot.log 2>&1`
- runs once a day at 11am and outputs a log file
- save & exit
- check with `crontab -l`

## Reset DB
- in testing the post, lots of stars set to `posted` when they weren't published
- `resetdb.py` resets all to unposted