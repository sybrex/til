import click
from til import app, bcrypt, reddit
from til.models import User, Til


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
        last_post = Til.objects(source=Til.SOURCE_REDDIT, author=subreddit).order_by('-created').first()
        code = last_post.code if last_post else None
        posts = reddit.fetch_posts(subreddit, code)
        for post in posts:
            post['source'] = Til.SOURCE_REDDIT
            til_post = Til(**post)
            til_post.save()
        print(f'{subreddit}: {len(posts)}')
