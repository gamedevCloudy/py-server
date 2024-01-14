from flask import Blueprint, render_template
from flask_login import login_required, current_user
# app = Flask(__name__)
main = Blueprint('main', __name__)

# Define the root route
@main.route('/')
def home():
    return render_template('index.html')

@main.route('/home')
def home_logout():
    return render_template('home.html')

@main.route('/profile')
@login_required
def profile(): 
    return render_template('profile.html', name=current_user.name)

@main.route('/levels')
def levels():
    return render_template('levels.html')


# in page elements
@main.route('/nav')
def nav(): 
    return render_template('nav.html')
