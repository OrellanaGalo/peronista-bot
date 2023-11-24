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

# List of users to follow
users_to_follow = ["@GaloOrellana12", "user2", "user3"]  # Add usernames of the
# users you want to follow

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def followAndRepostTweets():
    # Follow specified users
    for user_to_follow in users_to_follow:
        try:
            user = api.get_user(screen_name=user_to_follow)
            api.create_friendship(user.id)
            print(f"Followed: {user_to_follow}")
        except tweepy.TweepyException as e:
            print(f"Error following {user_to_follow}: {e}")
    # Fetch tweets from the specified topic from the users being followed
    for user_to_follow in users_to_follow:
        try:
            tweets = api.user_timeline(screen_name=user_to_follow, count=10, tweet_mode="extended")

            # Repost each tweet related to the specified topic
            for tweet in tweets:
                if topic.lower() in tweet.full_text.lower():
                    # Avoid retweeting tour own tweets to prevent loops
                    if tweet.user.screen_name != BOT_SCREEN_NAME:
                        # Retweet the tweet
                        api.retweet(tweet.id)
                        print(f"Retweeted from {user_to_follow}: {tweet.full_text}")

                        time.sleep(2)  # To avoid hitting rate limits
        except tweepy.TweepyException as e:
            print(f"Error fetching tweets from {user_to_follow}: {e}")


# Run the bot every 30 minutes
while True:
    followAndRepostTweets()
    time.sleep(1800)  # 30 minutes
