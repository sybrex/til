import tweepy
from til import app


TWEETS_LIMIT = 100


def twitter_client():
    auth = tweepy.OAuthHandler(app.config['TWITTER_API_KEY'], app.config['TWITTER_API_SECRET'])
    auth.set_access_token(app.config['TWITTER_ACCESS_TOKEN'], app.config['TWITTER_ACCESS_TOKEN_SECRET'])
    return tweepy.API(auth)


def fetch_posts():
    posts = []
    twitter = twitter_client()
    for tweet in twitter.home_timeline(count=TWEETS_LIMIT, tweet_mode='extended'):
        posts.append({
            'code': tweet.id_str,
            'author': tweet.user.name,
            'content':  tweet.full_text,
            'extended': '',
            'url': f'https://twitter.com/{tweet.user.screen_name}/status/{tweet.id_str}',
            'created': tweet.created_at
        })
    return posts
