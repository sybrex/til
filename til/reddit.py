from datetime import datetime
import praw
from til import app


def reddit_client():
    return praw.Reddit(
        username=app.config['REDDIT_USERNAME'],
        password=app.config['REDDIT_PASSWORD'],
        client_id=app.config['REDDIT_CLIENT_ID'],
        client_secret=app.config['REDDIT_CLIENT_SECRET'],
        user_agent=app.config['REDDIT_USER_AGENT'],
    )


def fetch_posts(subreddit, before=None):
    posts = []
    reddit = reddit_client()
    params = {'before': before} if before else None
    for submission in reddit.subreddit(subreddit).new(limit=10, params=params):
        posts.append({
            'code': submission.name,
            'author': submission.subreddit.display_name.lower(),
            'content': submission.title,
            'extended': submission.selftext if submission.is_self else '',
            'url': submission.url,
            'created': datetime.utcfromtimestamp(submission.created_utc)
        })
    return posts
