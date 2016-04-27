#!/usr/bin/python
import twitter
import sys

nargs = len(sys.argv)

if nargs != 2:
    print "USAGE: driver.py <api_keys_textfile>"
    sys.exit()

with open(sys.argv[1]) as f:
    api_keys = f.read().splitlines()

api = twitter.Api(consumer_key = api_keys[0],
                  consumer_secret = api_keys[1],
                  access_token_key = api_keys[2],
                  access_token_secret = api_keys[3])

statuses = api.GetUserTimeline(screen_name='justinbieber')

def get_latest_tweet(default=None):
    if statuses:
        return str(statuses[0].text)
    else:
        print "Failed to get tweet"
        sys.exit()
