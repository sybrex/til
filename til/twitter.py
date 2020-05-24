from datetime import datetime
import tweepy
from til import app


TWEETS_LIMIT = 5


def twitter_client():
    auth = tweepy.OAuthHandler(app.config['TWITTER_API_KEY'], app.config['TWITTER_API_SECRET'])
    auth.set_access_token(app.config['TWITTER_ACCESS_TOKEN'], app.config['TWITTER_ACCESS_TOKEN_SECRET'])
    return tweepy.API(auth)


def fetch_posts():
    posts = []
    twitter = twitter_client()
    for tweet in twitter.home_timeline(count=TWEETS_LIMIT):
        print(tweet.id)
        print(tweet.text)
        print(tweet.created_at)
        print(tweet.source)
        #print(tweet.user)
        # posts.append({
        #     'code': submission.name,
        #     'author': submission.subreddit.display_name.lower(),
        #     'content': submission.title,
        #     'extended': submission.selftext if submission.is_self else '',
        #     'url': submission.url,
        #     'created': datetime.utcfromtimestamp(submission.created_utc)
        # })
    return posts
