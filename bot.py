import tweepy
import time
from passwords import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET, TOPIC, BOT_SCREEN_NAME

# Replace with your API keys and access tokens
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_SECRET

# Set the topic you're interested in
topic = TOPIC

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def repost_tweets():
    # Search for tweets containing the specified topic
    tweets = api.search_tweets(q=topic, count=10)

    # Repost each tweet
    for tweet in tweets:
        try:
            # Avoid retweeting your own tweets to prevent loops
            if tweet.user.screen_name != BOT_SCREEN_NAME:
                api.retweet(tweet.id)
                print(f"Retweeted: {tweet.text}")
                time.sleep(2)  # To avoid hitting rate limits
        except tweepy.TweepyException as e:
            print(f"Error: {e}")


# Run the bot every 30 minutes
while True:
    repost_tweets()
    time.sleep(1800)  # 30 minutes
