#!/usr/bin/python
import twitter
import sys
import subprocess
import re
import requests
import os.path
from argparse import ArgumentParser

# **************************************
# ***********Initialization*************
# **************************************

ap = ArgumentParser(description='Change LED lighting based on sexy Justin Bieber\'s tweets')

ap.add_argument('--tweet',
                type=str,
                default='',
                help='Manually simulate a tweet')

ap.add_argument('--user',
                type=str,
                default='justinbieber',
                help='Set to follow a different Twitter user')

args = ap.parse_args()

with open('api-keys.txt') as f:
    api_keys = f.read().splitlines()

api = twitter.Api(consumer_key = api_keys[0],
                  consumer_secret = api_keys[1],
                  access_token_key = api_keys[2],
                  access_token_secret = api_keys[3])

statuses = api.GetUserTimeline(screen_name=args.user)

# ***************************************
# ************Helper Functions***********
# ***************************************

def save_prev_state(text):
    with open('prev_state', 'w') as f:
        f.write(text)

def get_prev_state():
    with open('prev_state', 'r') as f:
        return f.read()

def remove_urls(text):
    return re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','', text)

def get_tweet():
    if statuses:
        return remove_urls(str(statuses[0].text))
    else:
        print "Failed to get tweet"
        sys.exit()

def play_sound(text):
    cmd = ['gtts-cli.py', text, '-o', 'temp.mp3']
    cmd2 = ['mplayer', 'temp.mp3']
    cmd3 = ['rm', 'temp.mp3'] 
    with open('/dev/null', 'w') as outfile:
        subprocess.call(cmd, stdout=outfile)
        subprocess.call(cmd2, stdout=outfile)
        subprocess.call(cmd3, stdout=outfile)

def get_sentiment(text):
    r = requests.post('http://text-processing.com/api/sentiment/', data = {'text': text}).json()
    return r["label"]

def first_time_run():
    cmd = ['./transitionLEDs']
    if not args.tweet:
        tweet = get_tweet()
    else:
        tweet = args.tweet
    state = get_sentiment(tweet)
    if state == 'pos':
        cmd.append('initblue')
        subprocess.Popen(cmd)
    elif state == 'neg':
        cmd.append('initred')
        subprocess.Popen(cmd)
    elif state == 'neutral':
        cmd.append('initwhite')
        subprocess.Popen(cmd)
    save_prev_state(state)

def main():
    cmd = ['./transitionLEDs']
    if not args.tweet:
        tweet = get_tweet()
    else:
        tweet = args.tweet
    curr_state = get_sentiment(tweet)
    prev_state = get_prev_state()

    if prev_state == 'pos' and curr_state == 'neg':
        cmd.append('blue2red')
    elif prev_state == 'neg' and curr_state == 'pos':
        cmd.append('red2blue')
    elif prev_state == 'pos' and curr_state == 'neutral':
        cmd.append('blue2white')
    elif prev_state == 'neg' and curr_state == 'neutral':
        cmd.append('red2white')
    elif prev_state == 'neutral' and curr_state == 'pos':
        cmd.append('white2blue')
    elif prev_state == 'neutral' and curr_state == 'neg':
        cmd.append('white2red')
    elif prev_state == 'pos' and curr_state == 'pos':
        cmd.append('blue2blue')
    elif prev_state == 'neg' and curr_state == 'neg':
        cmd.append('red2red')
    elif prev_state == 'neutral' and curr_state == 'neutral':
        cmd.append('white2white')

    subprocess.Popen(cmd)
    play_sound(tweet)
    save_prev_state(curr_state)


# **********************************************
# ********************Main**********************
# **********************************************

if __name__ == "__main__":
    if not os.path.isfile('prev_state'):
        first_time_run()
    else:
        main()
