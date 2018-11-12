# Dependencies
from twarc import Twarc
import tweepy
import utils
import keys
import sys

# Set up dependencies for Twitter APIs
twarc = Twarc(keys.consumer_key, keys.consumer_secret,
              keys.access_token, keys.access_token_secret)

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

arguments = sys.argv # Get parameters from command line

if len(arguments) > 1:
  # If there's any arguments join with an OR in between
  hashtags = ' OR '.join(map(str, arguments)) 
else:
  # If no arguments don't run
  print("No arguments passed")
  sys.exit(0)

# Search Twitter for tweets conraining the hashtags
tweets = twarc.search(hashtags)

for tweet in tweets:
  user = tweet['user']
  
  # Check if tweet (not retweet) and determine if the user is an influencer
  if utils.not_retweet(tweet) and utils.is_influencer(tweet):

    # Check if you follow the influencer and if you've already sent a follow request
    if user['following'] == False and user['follow_request_sent'] == False:
      # Follow
      print('following: ' + user['name'])
      api.create_friendship(user['id'])

    # Check if they have more retweets than likes, like the tweet if not liked yet and viceversa
    if tweet['retweet_count'] >= tweet['favorite_count'] and tweet['favorited'] == False:
      
      # Like tweet
      print('liking')
      api.create_favorite(tweet['id'])
    elif tweet['retweeted'] == False:

      # Retweet
      print('retweeting')
      api.retweet(tweet['id'])
