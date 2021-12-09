import tweepy
import keys

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

carson = api.get_user('CallMeCarsonYT')
print(carson.id)
print()
print(carson.name)
print()
print(carson.screen_name)
print()
print(carson.description)