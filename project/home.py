from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Level
home = Blueprint('home', __name__)

@home.route('/app/nav')
def app_nav(): 
    return render_template('app.nav.html')

@home.route('/app')
@login_required
def homeRoute():
    return render_template('home.getlevels.html')

@home.route('/app/levels')
@login_required
def levels():
    levels = Level.query.order_by(Level.id).all()    
    return render_template('levels.html', levels=levels)

@home.route('/app/profile')
@login_required
def profile():
    return render_template('profile.html',name=current_user.name)

@home.route('/app-load')
def load(): 
    # return redirect('/app')
    return go_to_app

go_to_app = """<a href="/app"><button role="primary">Go To App</button></a>"""