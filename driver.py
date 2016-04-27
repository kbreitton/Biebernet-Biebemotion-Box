#!/usr/bin/python
import twitter
import sys
import subprocess
import re
import requests

curr_state = 'neutral'
prev_state = 'neutral'

with open('api-keys.txt') as f:
    api_keys = f.read().splitlines()

api = twitter.Api(consumer_key = api_keys[0],
                  consumer_secret = api_keys[1],
                  access_token_key = api_keys[2],
                  access_token_secret = api_keys[3])

statuses = api.GetUserTimeline(screen_name='justinbieber')

def remove_urls(text):
    return re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','', text)

def get_tweet():
    if statuses:
        return remove_urls(str(statuses[0].text))
    else:
        print "Failed to get tweet"
        sys.exit()

def play_sound(text):
    cmd = ['espeak', '-ven+f2', '-k5', text, '&'] 
    with open('/dev/null', 'w') as outfile:
        subprocess.call(cmd, stderr=outfile)

def get_sentiment(text):
    global curr_state
    r = requests.post('http://text-processing.com/api/sentiment/', data = {'text': text}).json()
    curr_state = r["label"]

def main():
    global curr_state
    global prev_state
    cmd = ['transitionLEDs'];
    tweet = get_tweet()
    get_sentiment(tweet)
    if prev_state == 'pos' and curr_state == 'neg':
        subprocess.Popen(cmd.append('blue2red'))
        prev_state = curr_state
    elif prev_state == 'neg' and curr_state == 'pos':
        subprocess.Popen(cmd.append('red2blue'))
        prev_state = curr_state
    elif prev_state == 'pos' and curr_state == 'neutral':
        subprocess.Popen(cmd.append('blue2white'))
        prev_state = curr_state
    elif prev_state == 'neg' and curr_state == 'neutral':
        subprocess.Popen(cmd.append('red2white'))
        prev_state = curr_state
    elif prev_state == 'neutral' and curr_state == 'pos':
        subprocess.Popen(cmd.append('white2blue'))
        prev_state = curr_state
    elif prev_state == 'neutral' and curr_state == 'neg':
        subprocess.Popen(cmd.append('white2red'))
        prev_state = curr_state
    play_sound(tweet)

if __name__ == "__main__":
    main()
