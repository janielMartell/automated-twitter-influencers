# Dependencies
import json

# Get influencer criteria from config.json file
config_file = open('config.json')
config = json.load(config_file)
influencer = config['influencer']


def is_influencer(tweet):
  """ Determines if an user who tweeted a tweet is an influencer """

  rts = tweet['retweet_count']
  fav = tweet['favorite_count']

  user = tweet['user'] 
  followers = user['followers_count']
  
  # Check if user meets the influencer Criteria
  if followers >= influencer['followers'] and rts >= influencer['retweets'] and fav >= influencer['likes']:
    return True
  else:
    return False


def not_retweet(tweet):
  """ Determines if it's tweet and not a retweet """

  # check if tweet has the retweeted status property, if so it's a retweet, if not it's original.
  if hasattr(tweet, 'retweeted_status'):
    return False
  else:
    return True
