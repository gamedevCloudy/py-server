import random

from project import db, models, create_app  # Assuming database instance is named 'db'
from project.models import Level
app = create_app()

with app.app_context():
    levels = Level.query.all()
    for level in levels:
        db.session.delete(level)

    for i in range(1, 6):  # Create 5 levels, named Level 1 to Level 5
        level = Level(
            name=f"Level {i}",  # Simple numerical naming
            description="Placeholder description for a safe and inclusive level",
            tests_required=random.randint(3),  # Set a random number of tests
            is_visible=i == 1  # Only the first level (Level 1) is visible initially
        )
        db.session.add(level)

    db.session.commit()  # Commit changes to the database
