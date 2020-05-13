import click
from til import app, bcrypt
from til.models import User


@app.cli.command('create-user')
@click.argument('name')
@click.argument('password')
def create_user(name, password):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=name, password=hashed_password)
    user.save()    
    print('User {} was added'.format(name))
