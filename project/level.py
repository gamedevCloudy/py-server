from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Level, UserProgress, Question, Answer

level = Blueprint('level', __name__)



@level.route('/app/level/<int:id>')  # Use <int:id> for type-checking
@login_required
def load_level(id):
    level = Level.query.get(id)  # Retrieve the level from the database

    if level:
        user_progress = UserProgress.query.filter_by(user_id=current_user.id, level_id=id).first()
        if user_progress:
            progress = (user_progress.sublevels_completed / level.tests_required) * 100
        else:
            progress = 0  # No progress if no entry in UserProgress

        return render_template('level.html', level=level, progress=progress)
    else:
        # Handle the case where the level doesn't exist
        return "Level not found", 404


# only the first render of question
@level.route('/app/level/<int:level_id>/<int:sublevel_id>')
@login_required
def load_test(level_id,sublevel_id):
   
    question = Question.query.filter_by(level_id=level_id, sublevel_index=sublevel_id).order_by(Question.id).first()
    answers = Answer.query.filter_by(question_id=question.id)

    return render_template('level.test.html', question=question, answers=answers)
 

@level.route('/app/level/check/<int:question_id>/<int:answer_id>')
@login_required
def check_answer(question_id, answer_id): 
    answers = Answer.query.filter_by(question_id=question_id).order_by(Answer.id)
    response = """"""
    for answer in answers:
        div= """"""
        if answer.id != answer_id:
            if answer.is_correct:
                div = f"""<div><button id={ answer.id} class="secondary outline correct" style="border: 1px lightgreen solid; transition: all ease-in 1s;">{answer.text}</button></div>"""
            else:
                div = f"""<div><button id={ answer.id} class="secondary outline" style="transition: all ease-in 1s ;">{answer.text}</button></div>"""
        else:
            if answer.is_correct:
                div = f"""<div><button id={ answer.id} class="secondary outline correct"  style="border: 1px lightgreen solid; transition: all ease-in 1s ;">{answer.text}</button></div>"""
            else:
                div = f"""<div><button id={ answer.id} class="secondary outline incorrect" style="border: 1px lightcoral solid; transition: all ease-in 1s ;">{answer.text}</button></div>"""

        response+=div
        response+="\n" 
    
    current_question = Question.query.filter_by(id=question_id).first()
    next_question = Question.query.filter(
        Question.id > current_question.id,  # Use `filter` for arbitrary expressions
        Question.level_id == current_question.level_id,
        Question.sublevel_index == current_question.sublevel_index
    ).order_by(Question.id).first()  # Order by ID for correct sequencing

    if(next_question != None): 
        requestNextQuestion=f"""<div 
        hx-get="/app/level/question/{ next_question.id }"
        hx-swap="innerHTML"
        hx-target="#swappable"
        hx-trigger="load delay:1200ms"
        >""" 
        return response+requestNextQuestion
    else: 
        success_screen=f"""<div 
        hx-get="/app/level/success/{current_question.level_id}/{current_question.sublevel_index}"
        hx-swap="innerHTML"
        hx-target="#swappable"
        hx-trigger="load delay:1200ms"
        >""" 
        # redirect to checkpoint/level success 
        return response+success_screen



@level.route('/app/level/question/<int:question_id>')
@login_required
def request_by_question_id(question_id): 
    question = Question.query.filter_by(id=question_id).first()
    answers=Answer.query.filter_by(question_id=question_id)
    
    return render_template('level.question.html', question=question, answers=answers)

@level.route('/app/level/success/<int:level_id>/<int:sublevel_index>')
@login_required
def success_screen(level_id, sublevel_index): 
    success = f"""<div>
    <h1>Congratulations!!!</h1>
    <h2>You have completed checkpoint { sublevel_index } of level { level_id }</h2>
    <a
    href="/app"
    role="button"
    class="primary outline"
    >
    Continue
    </a>
    </div>"""

    return success