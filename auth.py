from flask import request, Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, logout_user, login_user

from model.authenticated_user import AuthenticatedUser
from model.user_details import UserDetails
from service import user_service

auth = Blueprint('auth', __name__)


@auth.route("/login")
def login():
    return render_template('login.html')


@auth.route("/login", methods=['POST'])
def login_post():
    user_name = request.form.get('user_name')
    user_password = request.form.get('user_password')

    is_authenticated = user_service.try_login_user(user_name, user_password)
    if not is_authenticated:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    user = user_service.get_user_by_user_name(user_name)

    if user:
        login_user(AuthenticatedUser(user))
    return redirect(url_for('main.index'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/register')
def register():
    return render_template('register.html')


@auth.route("/register", methods=['POST'])
def register_post():
    name = request.form.get('user_name')
    username = request.form.get('user_username')
    password = request.form.get('user_password')
    email = request.form.get('user_email')

    if user_service.user_exists(username):
        return redirect(url_for('auth.signup'))

    user_details = UserDetails(0, name, email, username, password)
    user_service.register_new_user(user_details)
    return redirect(url_for('auth.login'))
