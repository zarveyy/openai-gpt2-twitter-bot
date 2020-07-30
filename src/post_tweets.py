import gpt_2_simple as gpt2
from datetime import datetime
import tweepy
import random
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def excluded(word):
    for x in ["@","http","kill"]:
        if word.find(x) != -1:
            return True
    return False

def post_tweets():
    session = gpt2.start_tf_sess()
    while True:
        gpt2.generate_to_file(
            session, destination_path="generated_tweets.txt", run_name="run1")

        with open("generated_tweets.txt", "r", encoding="utf-8") as in_file:
            tweets = in_file.read().split("\n\n")

        while len(tweets) > 1:
            idx = random.randrange(0, len(tweets))
            tweet = tweets.pop(idx).split(" ")
            tweet = " ".join(word for word in tweet if not excluded(word))
            if len(tweet) < 15:
                continue
            print(tweet)
            api.update_status(tweet)
            time.sleep(12*60*60)

if __name__ == "__main__":
    post_tweets()