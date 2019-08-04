# import tweepy and time for tweeting scheduly
import tweepy
import time
import requests
import os

# funtion for initiating Twitter API
def init_twitter():
	# Consumer keys and access tokens, used for OAuth
	consumer_key = ''
	consumer_secret = ''
	access_token = ''
	access_token_secret = ''

	# OAuth process, using the keys and tokens
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	 
	# Creation of the actual interface, using authentication
	api = tweepy.API(auth)
	return api

# tweet with image and caption
def tweet_with_image(url, status):
 
	filename = 'temp.jpg'
 #    request = requests.get(url, stream=True)
 #    if request.status_code == 200:
 #        with open(filename, 'wb') as image:
 #            for chunk in request:
 #                image.write(chunk)
 #        api.update_with_media(filename, status=message)
 #        os.remove(filename)
 #    else:
 #        print("Unable to download image")
	
	# # Send the tweet.
	# api.update_with_media(imagePath, status)

#api = init_twitter()

with open('status.txt', "r") as f:
	for i in f:
		print (i.split('; ')[0], i.split('; ')[1])
		#tweet_with_image(i.split('; ')[0], i.split('; ')[1])
		time.sleep(1800)
