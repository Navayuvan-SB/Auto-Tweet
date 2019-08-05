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
def tweet_with_image(url):
 
	filename = 'temp.jpg'
	request = requests.get(url, stream=True)
	if request.status_code == 200:
		with open(filename, 'wb') as image:
			for chunk in request:
				image.write(chunk)
		with open('temp.txt', 'r') as f:
			api.update_with_media(filename, status=f.read())
			os.remove(filename)
	else:
		print("Unable to download image")

def check_limit(text):

	if (len(text) > 276):

		print (len(text) - 280)
		return False

	else:

		return True

# two lists for storing image link and caption
status = []
images = []

# drive header to get image link active
drive_header = 'https://drive.google.com/uc?export=view&id='

# initiating twitter API
api = init_twitter()

# Captioning the images
status.append('When you wrote a #fibonacci program and our family members thought we developed a hard-core software.. 😅😂🤣\n\nEver happened to you??\n\n#programming #coding #developer #javascript #technology #code #html #python #java #tech #webdesign #linux #php #codinglife #design #hacking')
status.append("I'm always a Copy #learner..😅 \n\nWhat about you?\n\n#programming #coding #programmer #developer #javascript #technology #code #html #python #java #tech #css #webdesign #software #linux #computer #php #codinglife #programmers #android #design #hacking")
status.append("Why should be use quotes for string?? 😅😂🤣\n\nWhat's the most stupid thing you have searched on #stackoverflow \n\n#programming #coding #developer #javascript #technology #code #html #python #java #tech #css #webdesign #linux #php #codinglife #design #hacking")
status.append("Critical situation, right? 😹 \n\nEver happened to you guys? \n\n#programming #coding #programmer #developer #javascript #technology #code #html #python #java #tech #css #webdesign #software #linux #computer #php #codinglife #programmers #android #design #hacking")
status.append("A #Product's greatest strength is it's UI/UX. Agree?? 🤯😈 \n\nHow many of you are Front-end developers??\n\n#programming #coding #developer #javascript #technology #code #html #python #java #tech #css #webdesign #linux #php #codinglife #design #hacking")
status.append("How should a developer propose his crush..? 🤥🤔\n\nWell, here is the answer for that? 😂🤣\n\n#programming #coding #developer #javascript #technology #code #html #python #java #tech #css #webdesign #linux #php #codinglife #design #hacking")
status.append("Just do it..!! 😈 \n\nWhat's your favorite project? comment the github link below? \n\n#programming #coding #developer #javascript #technology #code #html #python #java #tech #css #webdesign #linux #php #codinglife #design #hacking")
status.append("Yeah, I'm still worthy....!!!!😅 \n\n#programming #coding #programmer #developer #javascript #technology #code #html #python #java #tech #css #webdesign #software #linux #computer #php #codinglife #programmers #android #design #hacking")
status.append("#Android_Studio things...!! 😅😂🤣 \n\nHave you ever undergone this situation?? \n\n#programming #coding #programmer #developer #javascript #technology #code #html #python #java #tech #css #webdesign #software #linux #computer #php #codinglife #programmers #android #design #hacking")
status.append("I'm not did it..!! Only my code do that..😅😂🤣\n\n#programming #coding #programmer #developer #javascript #technology #code #html #python #java #tech #css #webdesign #software #linux #computer #php #codinglife #programmers #android #design #hacking")

images.append("1LKS1CGjlvdHjGv_3gLGmF-r8Hqig1eU4")
images.append("1CQ8hR-4xw0c0pnnp8Sq7CKmwNzvk3waO")
images.append("1dX7kleTH0Zam4ix1gEw2hm-3QQnjr5pR")
images.append("1itisiL_T_zkmJf9hpYrZiZVnXXC0g4bW")
images.append("1UnCqgg-war0okSLM6fqsWlScmP787ADw")
images.append("1LlhzgtWvPMgQQm8tsPTJbNCUPIDJuhIL")	
images.append("1ptIpLJzMD1FzO8DS5Qaup_NfJhYb9JZ_")
images.append("1E40yMIbhipiFmGo4SAQEzf8aUfZPSqzx")
images.append("1JfXwgoX0bur59irxUzFWutTmncyGZlQn")
images.append("1iwLfVtj0KoHmcM_NQTp3JLuAmflvQsq7")


#looping to tweet at particular interval
for i in range(len(status)):
	with open('temp.txt', 'w') as f:
			f.write(status[i])
	tweet_with_image(drive_header + images[i])
	print ("Tweeted")
	time.sleep(3)
