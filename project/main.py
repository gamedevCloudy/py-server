from flask import Blueprint, render_template

# app = Flask(__name__)
main = Blueprint('main', __name__)

# Define the root route
@main.route('/')
def home():
    return render_template('index.html')


@main.route('/levels')
def levels():
    return render_template('levels.html')


# in page elements
@main.route('/nav')
def nav(): 
    return render_template('nav.html')
