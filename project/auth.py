from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db 
from flask_login import login_user, login_required, logout_user


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login(): 
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        return invalid_credentails

    login_user(user, remember=remember)
    return loggin_in


@auth.route('/signup')
def signup(): 
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    #validate and create new user
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user: # if a user is found, we want to redirect back to signup page so user can try again

        return user_exists

     # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method="scrypt"))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return signup_success



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return logging_out

user_exists = """<article hx-get="/login" hx-target="#swappable" hx-trigger="load delay:1200ms" hx-swap="innerHTML"><p aria-busy="true">User already exists.</p></article>"""
signup_success = """<article hx-get="/login" hx-target="#swappable" hx-trigger="load delay:1200ms" hx-swap="innerHTML"><p aria-busy="true">Account created, please login.</p></article>"""

invalid_credentails = """<article hx-get="/login" hx-target="#swappable" hx-trigger="load delay:1200ms" hx-swap="innerHTML"><p aria-busy="true">Invalid credentials.</p></article>"""

# loggin_in = """<article hx-get="/app-load" hx-trigger="load delay:1200ms" hx-redirect hx-push-url="/app"><p aria-busy="true">Logging in...</p></article>"""
loggin_in = """<article hx-get="/app-load" hx-trigger="load delay:1200ms"  hx-redirect ><p aria-busy="true">Logging in...</p></article>"""

logging_out= """<article hx-get="/logout-success" hx-target="#swappable" hx-trigger="load delay:1200ms" hx-swap="innerHTML"><p aria-busy="true">Logging out...</p></article>"""
