import tweepy
import twitter_credentials as tc
import random
import time

auth = tweepy.OAuthHandler(tc.consumer_key, tc.consumer_secret)
auth.set_access_token(tc.access_token, tc.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def download_all_tweets(user):
    page_list = []

    for page in tweepy.Cursor(api.user_timeline, screen_name=user, tweet_mode='extended').pages():
        page_list.append(page)

    with open("downloaded_tweets.csv","a",encoding="utf-8") as out_file:
        for page in page_list:
            for status in page:
                if not status.retweeted:
                    out_file.write(status.full_text + "\n\n")
                    print(status.full_text)

if __name__ == "__main__":
    for user in ["TwitterUsername"]:
        download_all_tweets(user)