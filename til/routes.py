import os
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from til import app, bcrypt, forms
from til.models import User


@app.context_processor
def inject_year():
    return dict(year=datetime.now().year)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/admin/login', methods=['GET', 'POST'])    
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():        
        user = User.objects(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('admin/login.html', form=form)


@app.route('/admin/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
