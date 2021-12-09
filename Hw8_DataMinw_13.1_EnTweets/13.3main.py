import tweepy
import sys
import keys
from tweepy import Stream
from tweepy.streaming import StreamListener

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
def main():

    count = 0
    tweets = api.search(q="#venting", lang="en", count=10000)

    for tweet in tweets:
        try:
            if tweet.extended_tweet["full_text"]:#tweet.full_text:
                #print(tweet.full_text)
                count += 1
        except:
            pass
    print("Percent of Extended Tweets out of 10,000 tweets: ",(count/10000), "%")

main()