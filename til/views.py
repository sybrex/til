from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, login_required
from til import app, bcrypt, forms
from til.models import User, Til
from datetime import datetime
import uuid


@app.route('/')
def home():
    posts = Til.objects(visible=True).order_by('-created')
    return render_template('home.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('current'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/current')
@login_required
def current():
    posts = Til.objects(status=Til.STATUS_CURRENT).order_by('-created')
    return render_template('current.html', posts=posts)


@app.route('/backlog')
@login_required
def backlog():
    posts = Til.objects(status=Til.STATUS_BACKLOG).order_by('-created')
    return render_template('backlog.html', posts=posts)


@app.route('/icebox')
@login_required
def icebox():
    posts = Til.objects(status=Til.STATUS_ICEBOX).order_by('-created')
    return render_template('icebox.html', posts=posts)


@app.route('/tils/<id>', methods=['POST', 'GET'])
@login_required
def update_til(id):
    til_post = Til.objects(code=id).get()
    form = forms.TilForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            til_post.content = form.title.data
            til_post.extended = form.content.data
            til_post.save()
            flash('Post was updated', 'success')
            return redirect(url_for('current'))
    else:
        form.title.data = til_post.content
        form.content.data = til_post.extended
        return render_template('til.html', form=form, action='update_til', id=id)


@app.route('/tils/<id>/delete', methods=['POST'])
@login_required
def remove_til(id):
    til_post = Til.objects(code=id).get()
    til_post.delete()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('current'))


@app.route('/tils/create', methods=['POST', 'GET'])
@login_required
def create_til():
    form = forms.TilForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            til_post = Til(
                code=str(uuid.uuid4()),
                source=Til.SOURCE_ME,
                author='',
                content=form.title.data,
                extended=form.content.data,
                url='/',
                created=datetime.now(),
                status=Til.STATUS_CURRENT
            )
            til_post.save()
            flash('Your post has been created', 'success')
            return redirect(url_for('current'))
    else:
        return render_template('til.html', form=form, action='create_til', id=None)


@app.route('/status', methods=['POST'])
@login_required
def til_status():
    status = request.form.get('status')
    ids = request.form.getlist('ids[]')
    if any(status in code for code in Til.STATUSES) and len(ids) > 0:
        Til.objects(code__in=ids).update(set__status=status)
        return {'status': True}
    else:
        return {'status': False}


@app.route('/toggle_visible', methods=['POST'])
@login_required
def toggle_visible():
    try:
        post = Til.objects(code=request.form.get('id')).get()
        post.visible = not post.visible
        post.save()
        return {'status': True, 'visible': post.visible}
    except Til.DoesNotExist:
        return {'status': False}
