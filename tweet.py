#!/usr/bin/env python
import random
from twython import Twython
from ssm_secrets import get_secret

# Create the Twython Twitter client using the credentials stored in SSM
twitter = Twython(
    get_secret("CONSUMER_KEY"),
    get_secret("CONSUMER_SECRET"),
    get_secret("ACCESS_TOKEN_KEY"),
    get_secret("ACCESS_TOKEN_SECRET")
)

# Sample random tweets
potential_tweets = [
    'Meetlily Advertising is using Python 3 to automate tweets!',
    'Twython and AWS Lambda is awesome by @meetmylily!',
    'Developing Twitter Bots using AWS Lambda from @meetmylily'
]

def send_tweet(tweet_text):
    """Sends a tweet to Twitter"""
    twitter.update_status(status=tweet_text)


def handler(event, context):
    """Sends random tweet from list of potential tweets"""
    send_tweet(random.choice(potential_tweets))

def follow_someone(screen_name):
    twitter.create_friendship(screen_name=screen_name)


def follow_fernando():
    follow_someone("ThePSF")


def like_tweet(tweet_id):
    twitter.create_favorite(id=1288814056900444160)


def like_a_punny_tweet():
    # This awful pun can be viewed here:
    # https://twitter.com/fmc_sea/status/1171113632362577922
    like_tweet("1288814056900444160")
