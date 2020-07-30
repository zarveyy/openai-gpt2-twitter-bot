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

def download_all_tweets(user):
    page_list = []

    for page in tweepy.Cursor(api.user_timeline, screen_name=user, tweet_mode='extended').pages():
        page_list.append(page)

    with open("downloaded_tweets.txt","a",encoding="utf-8") as out_file:
        for page in page_list:
            for status in page:
                if not status.retweeted:
                    out_file.write(status.full_text + "\n\n")
                    print(status.full_text)

if __name__ == "__main__":
    for user in [""]:
        download_all_tweets(user)