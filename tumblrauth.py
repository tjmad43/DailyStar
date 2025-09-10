import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session

# Load env vars
load_dotenv()
TUMBLR_CONSUMER_KEY = os.getenv("TUMBLR_CONSUMER_KEY")
TUMBLR_CONSUMER_SECRET = os.getenv("TUMBLR_CONSUMER_SECRET")
BLOG_NAME = os.getenv("BLOG_NAME")

# Get request token
# Make sure app has a valid callback URL set, e.g., http://127.0.0.1/callback
request_token_url = 'https://www.tumblr.com/oauth/request_token'
oauth = OAuth1Session(
    TUMBLR_CONSUMER_KEY,
    client_secret=TUMBLR_CONSUMER_SECRET,
    callback_uri='http://localhost/callback'
)
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

print("Request Token:", resource_owner_key)
print("Request Token Secret:", resource_owner_secret)

# Authorize the app
base_authorization_url = 'https://www.tumblr.com/oauth/authorize'
authorization_url = oauth.authorization_url(base_authorization_url)
print("\nGo to this URL in your browser, log in, and authorize the app:")
print(authorization_url)

# Paste verifier code 
verifier = input('Paste the verifier code here: ')

# Get access token
access_token_url = 'https://www.tumblr.com/oauth/access_token'
oauth = OAuth1Session(
    TUMBLR_CONSUMER_KEY,
    client_secret=TUMBLR_CONSUMER_SECRET,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

print("\nYour OAuth credentials:")
print("OAuth Token:", oauth_tokens['oauth_token'])
print("OAuth Secret:", oauth_tokens['oauth_token_secret'])
