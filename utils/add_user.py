from project import db, create_app
from project.models import User
app = create_app()

with app.app_context(): 
    u = User(email="user@site.com", password="password", name ="user1")
    db.session.add(u)
    db.session.commit()

