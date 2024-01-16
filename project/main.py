from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)


# Define the root route
@main.route('/')
def home():
    return render_template('index.html')

@main.route('/logout-success')
def logout_success():
    return render_template('logged_out.html')

@main.route('/profile')
@login_required
def profile(): 
    return render_template('profile.html', name=current_user.name)

# in page elements
@main.route('/nav')
def nav(): 
    return render_template('nav.html')




