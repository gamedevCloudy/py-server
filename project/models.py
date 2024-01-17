from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Level(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    tests_required = db.Column(db.Integer, default=3) 
    # isUnlocked = db.Column(db.Boolean, default=False)
    
    is_visible = db.Column(db.Boolean, default=False)

class UserProgress(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), primary_key=True)
    completed = db.Column(db.Boolean, default=False)
    sublevels_completed = db.Column(db.Integer, default=0)
    score = db.Column(db.Integer)
    attempts = db.Column(db.Integer, default=0)
    # completion_time = db.Column(db.DateTime)

    # Add other relevant fields based on your requirements

    user = db.relationship('User', backref='progress')
    level = db.relationship('Level', backref='progress')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)
    sublevel_index = db.Column(db.Integer, nullable=False)  # New field for sublevel association
    text = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(255))  # Optional image path

    answers = db.relationship('Answer', backref='question', lazy=True)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
    image_path = db.Column(db.String(255))  # Optional image path