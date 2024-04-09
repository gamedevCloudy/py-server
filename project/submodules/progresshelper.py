from flask_login import login_required, current_user
from .. import db
from ..models import Level, UserProgress, Question, Answer



def updateProgress(level_id):
    progress = UserProgress.query.filter_by(user_id=current_user.id, level_id=level_id).first() 
    if progress == None:
        # create new entry
        prog =UserProgress(user_id=current_user.id, level_id=level_id, attempts=1, score=0)
        db.session.add(prog)
        db.session.commit()
    else: 
        db.session.delete(progress)
        progress.attempts+=1
        db.session.add(progress)
        db.session.commit()


def updateSublevelProgress(level_id, sublevel_index):
    progress = UserProgress.query.filter_by(user_id=current_user.id, level_id=level_id).first() 
    db.session.delete(progress)
    progress.sublevels_completed +=1
    if progress.score == None: 
        progress.score = 0
    progress.score += 100
    # level completed only if
    if(sublevel_index == 3): 
        progress.completed = True; 

    db.session.add(progress)
    db.session.commit()