import tweepy
import json
import urllib2
import random
from apscheduler.scheduler import Scheduler # You'll need apscheduler for this
from datetime import datetime

def post_twitter(status):
	consumer_key=""
	consumer_secret=""

	access_token=""
	access_token_secret=""

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	api.update_status(status)

def get_top_r_funny():
	data = json.load(urllib2.urlopen("http://www.reddit.com/r/funny.json"))
	posts = [post['data'] for post in data['data']['children']]
	for post in posts:
		if 'imgur.com' in post['url']:
			return str(post['url'])

def get_funny_phrase():
	phrases = ['lol', 'smh', 'check it', 'haha', 'I can\'t deal with this!', 'Too funny', 'Woah', 'too much']
	return random.choice(phrases)

def get_random_hashtag():
	hashtags = ["#momquotes", '#AwkwardDate', '#LMAO', '#TheInternet']
	return random.choice(hashtags)

def post_tweet():
	phrase = get_funny_phrase()
	top_link = get_top_r_funny()
	hashtag = get_random_hashtag()
	post_twitter(phrase + ' ' + top_link + ' ' + hashtag)

post_tweet()