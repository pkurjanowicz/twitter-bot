import os
import sys
import tweepy

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_KEY = os.getenv('ACCESS_KEY')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')
try:
    if not (CONSUMER_KEY and CONSUMER_SECRET and ACCESS_KEY and ACCESS_SECRET):
        from secrets import (
            CONSUMER_KEY,
            CONSUMER_SECRET,
            ACCESS_KEY,
            ACCESS_SECRET)
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    assert api.verify_credentials()
except ImportError:
    print(
        """Uh oh, we hit a problem. Maybe one of these is the problem?
  a) You're running locally, but haven't finished making your secrets.py file
  b) You're deploying to heroku, but forgot to set the environment variables?
""", file=sys.stderr)
    sys.exit(1)
except AssertionError:
    print("We weren't able to login to twitter with the values you gave us.",
          file=sys.stderr)
    print("Maybe double check them?", file=sys.stderr)
    sys.exit(1)
