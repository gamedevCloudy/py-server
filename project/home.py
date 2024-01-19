from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Level, UserProgress
home = Blueprint('home', __name__)

@home.route('/app/nav')
def app_nav(): 
    return render_template('home.nav.html')

@home.route('/app')
@login_required
def homeRoute():
    return render_template('home.getlevels.html')

@home.route('/app/levels')
@login_required
def levels():
    user = current_user
    levels = Level.query.order_by(Level.id).all()
    progress = UserProgress.query.filter_by(user_id=user.id).all()

    # Determine highest completed level (or 0 if none completed)
    highest_completed_level = max(progress, key=lambda p: p.level_id).level_id if progress else 0

    # Mark all levels as visible initially
    for level in levels:
        level.is_visible = True

    # Restrict visibility for levels beyond the highest completed level + 1 (except level 1)
    for level in levels[1:]:  # Skip the first level
        if level.id > highest_completed_level + 1:
            level.is_visible = False

    return render_template('home.levels.html', levels=levels, progress=progress)




@home.route('/app/profile')
@login_required
def profile():
    return render_template('profile.html',name=current_user.name)

@home.route('/app-load')
def load(): 
    # return redirect('/app')
    return go_to_app

go_to_app = """<a href="/app"><button role="primary">Go To App</button></a>"""