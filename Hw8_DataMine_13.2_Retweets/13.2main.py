# if rt


import time
import tweepy
import sys
import keys
from tweepy import Stream
from tweepy.streaming import StreamListener

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# intializing retweet counter with zero
counter = 0

# fetching the statuses and looping through every status.id and counting its retweets
for tweet in tweepy.Cursor(api.home_timeline, screen_name = 'CallMeCarsonYT') .items(10000):

    try:
        tweettext = str(tweet.text.lower().encode('ascii', errors='ignore'))
    #print(tweettext)

        if tweettext.startswith("b'rt @") == True:
            counter += 1
    except tweepy.RateLimitError:
        time.sleep(60 * 15)
        pass




#for tweet in tweepy.Cursor(api.search, q='trump',tweet_mode='extended').items(100):
    # Defining Tweets Creators Name
 #   tweettext = str( tweet.full_text.lower().encode('ascii',errors='ignore')) #encoding to get rid of characters that may not be able to be displayed
    # Defining Tweets Id
  #  if tweettext.startswith("rt @") == True:
   #     counter+=1










print(counter)
#print(count)
print("Percent of Retweets Out of 10,000 tweets is: ", (counter/10000),"%")
'''tweets = api.search(q="#cats", lang="en", count=10000)
count = 0

for tweet in tweets:
    try:
        if tweet.retweeted:
            count += 1
    except:
        continue
'''



