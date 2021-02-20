import tweepy
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("########", "##########")
auth.set_access_token("########", "######")     #checkout key_format.py

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

search='#MachineLearning'

TweetNum=1000

user=api.me()

for tweet in tweepy.Cursor(api.search, search).items(TweetNum):
  try:
    tweet.favorite()
    time.sleep(20)
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break
