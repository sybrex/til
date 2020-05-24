import click
from til import app, bcrypt, reddit, twitter
from til.models import User, Til
from mongoengine import NotUniqueError


@app.cli.command('create-user')
@click.argument('name')
@click.argument('password')
def create_user(name, password):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=name, password=hashed_password)
    user.save()    
    print('User {} was added'.format(name))


@app.cli.command('reddit-sync')
def reddit_sync():
    for subreddit in app.config['REDDIT_SUBREDDITS']:
        posts = reddit.fetch_posts(subreddit)
        new_posts_count = 0
        for post in posts:
            post['source'] = Til.SOURCE_REDDIT
            til_post = Til(**post)
            try:
                til_post.save()
                new_posts_count += 1
            except NotUniqueError:
                pass
        print(f'{subreddit}: {new_posts_count}')


@app.cli.command('twitter-sync')
def twitter_sync():
    posts = twitter.fetch_posts()
    new_posts_count = 0
    for post in posts:
        post['source'] = Til.SOURCE_TWITTER
        print(post)
        til_post = Til(**post)
     #   try:
      #      til_post.save()
       #     new_posts_count += 1
       # except NotUniqueError:
        #    pass
    print(f'New tweets: {new_posts_count}')
