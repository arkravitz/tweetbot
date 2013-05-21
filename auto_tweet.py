import tweepy
import json
import urllib2
import random

def post_twitter(status):
	''' Logs into twitter using the tweepy api and posts the parameter status'''

	# Find these after creating an app on twitter
	consumer_key=""
	consumer_secret=""
	access_token=""
	access_token_secret=""

	# Authorize for twitter
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	# Post the status
	api.update_status(status)

def get_top_r_funny():
	''' Gets the top r/funny imgur post from reddit and returns the url of the post. '''
	data = json.load(urllib2.urlopen("http://www.reddit.com/r/funny.json"))
	posts = [post['data'] for post in data['data']['children']]
	for post in posts:
		if 'imgur.com' in post['url']:
			return str(post['url'])

def get_funny_phrase():
	''' Returns a random phrase from the list of phrases. '''
	phrases = ['lol', 'smh', 'check it', 'haha', 'I can\'t deal with this!', 'Too funny', 'Woah', 'too much']
	return random.choice(phrases)

def get_random_hashtag():
	''' Returns a random hashtag from the list of hashtags. '''
	hashtags = ["#momquotes", '#AwkwardDate', '#LMAO', '#TheInternet']
	return random.choice(hashtags)

def post_tweet():
	''' Adds together the phrase, the top reddit link, and the hashtag
	and then posts the result to twitter. '''
	phrase = get_funny_phrase()
	top_link = get_top_r_funny()
	hashtag = get_random_hashtag()
	post_twitter(phrase + ' ' + top_link + ' ' + hashtag)

post_tweet()