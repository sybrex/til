from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, login_required
from datetime import datetime
from til import app, bcrypt, forms
from til.models import User, Til


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


@app.route('/status', methods=['POST'])
@login_required
def til_status():
    status = request.form.get('status')
    ids = request.form.getlist('ids[]')
    print(status)
    print(ids)
    if any(status in code for code in Til.STATUSES) and len(ids) > 0:
        Til.objects(code__in=ids).update(set__status=status)
        return {'status': True}
    else:
        return {'status': False}
