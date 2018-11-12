# Automate finding influential people on Twitter  

This is a very simple script to automate finding, following, and retweeting/liking influential people
of a topic on Twitter.

First of all go to `keys.py` and replace the keys with your own, [find them here](https://developer.twitter.com/), it'll look a little bit like so:

```python
# keys.py

consumer_key = "YOUR_KEY_HERE"
consumer_secret = "YOUR_SECRET_KEY_HERE"
access_token = "YOUR_TOKEN_HERE"
access_token_secret = "YOUR_SECRET_TOKEN_HERE"
```

Go to the `config.json` file and configure what you consider to be an influential person it'll look something like this by default:

```javascript
// config.json
{
  "influencer": {
    "followers": 1000,
    "likes": 100,
    "retweets": 100
  }
}
```

Lastly run `python main.py` followed by the topics you are interested in e.g. `blockchain` like so:

```bash
python main.py blockchain
# replace blockchain with whatever topic you're interested in
```