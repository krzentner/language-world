

For the final line of your program, use the same `push()` command as the program `drawer_open` uses, but pass a different argument.
'''

'''
# push: slide the puck to the target location
def push(robot):
    if check("the puck is right of the robot's gripper"):
        robot.put("gripper behind puck")
    if check("the puck is forward aligned with the robot's gripper"):
        robot.push("puck to goal")
'''
[eod] [code]from flask import render_template, redirect, url_for, request, flash
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm, ChangePasswordForm
from ..email import send_email


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if not next or url_parse(next).netloc != '':
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account',
                   'auth/email/confirm', user=user, token=token)
        flash('A confirmation email has been sent to you by email.'