#this script unfollows everyone that does not follow you back on twitter
#you need developers access on twitter to be able to run this bot
#I've been able to successfully deploy this script to unfollow around 2k accounts at once.
#I cannot give assurance that further usage MAY not lead to a suspension from twitter. 
#I don't know what the rules are but if you unfollow too many people at a go on twitter, they might suspend you account for some time.
import tweepy


CONSUMER_KEY ='input ypour consumer key here'
CONSUMER_SECRET ='input your consumer secret here'
ACCESS_KEY ='input your access key here'
ACCESS_SECRET = 'your access secret goes here'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#this checks up all your followed id
followers = api.followers_ids()
#this confirms if the followed also follow back -hence friends
friends = api.friends_ids()
#I'm just joking they're not bastards, they're ----cheats! (smiles)
print("let's unfollow these bastards!")

def unfollow():
	for followed in friends:
		if followed not in followers:
			api.destroy_friendship(followed)
			
while True:
    unfollow()
    
	
	
