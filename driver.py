#!/usr/bin/python
import twitter
import sys
import subprocess
import re

with open('api-keys.txt') as f:
    api_keys = f.read().splitlines()

api = twitter.Api(consumer_key = api_keys[0],
                  consumer_secret = api_keys[1],
                  access_token_key = api_keys[2],
                  access_token_secret = api_keys[3])

statuses = api.GetUserTimeline(screen_name='justinbieber')

def remove_urls(text):
    return re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','', text)

def get_latest_tweet(default=None):
    if statuses:
        return remove_urls(str(statuses[0].text))
    else:
        print "Failed to get tweet"
        sys.exit()

def play_sound(text):
    cmd = ["espeak", "-ven+f5", "-k5", text, "&"] 
    with open("/dev/null", "w") as outfile:
        subprocess.call(cmd, stderr=outfile)
