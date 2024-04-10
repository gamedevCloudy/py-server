import random

from .. import db, models, create_app  # Assuming database instance is named 'db'
from ..models import Question, Answer
app = create_app()

with app.app_context(): 
    for sublevel_index in range(1,4): 
        for question_number in range(1,6): 
            question = Question(
                level_id=1,
                sublevel_index=sublevel_index,
                text=f"Dummy question for level {1} {sublevel_index} {question_number}",
            )
            db.session.add(question)
            db.session.commit()
            answer = Answer(question_id=question.id, text="Answer 1", is_correct=False)
            answer1 = Answer(question_id=question.id, text="Answer 2", is_correct=False)
            answer2= Answer(question_id=question.id, text="Answer 3", is_correct=False)
            answer3 = Answer(question_id=question.id, text="Answer 4", is_correct=True)
            
            db.session.add(question)
            db.session.add_all([answer,answer1,answer2,answer3])
    
    db.session.commit()

    print("Dummy questions added successfully!")