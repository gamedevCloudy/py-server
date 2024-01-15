from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

home = Blueprint('home', __name__)

@home.route('/app/nav')
def app_nav(): 
    return render_template('app.nav.html')

@home.route('/app')
@login_required
def homeRoute():
    return render_template('home.html')

@home.route('/app-load')
def load(): 
    # return redirect('/app')
    return go_to_app

go_to_app = """<a href="/app"><button role="primary">Go To App</button></a>"""