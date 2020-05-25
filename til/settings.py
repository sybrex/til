from os import environ


DEBUG = environ.get('DEBUG')
SECRET_KEY = environ.get('SECRET_KEY')

MONGODB_HOST = environ.get('MONGODB_HOST')
MONGODB_DB = environ.get('MONGODB_DB')
MONGODB_PORT = int(environ.get('MONGODB_PORT'))

REDDIT_USERNAME = environ.get('REDDIT_USERNAME')
REDDIT_PASSWORD = environ.get('REDDIT_PASSWORD')
REDDIT_CLIENT_ID = environ.get('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = environ.get('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = environ.get('REDDIT_USER_AGENT')
REDDIT_SUBREDDITS = environ.get('REDDIT_SUBREDDITS').split(',')

TWITTER_API_KEY = environ.get('TWITTER_API_KEY')
TWITTER_API_SECRET = environ.get('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = environ.get('TWITTER_ACCESS_TOKEN_SECRET')