import random

from project import db, models, create_app  # Assuming database instance is named 'db'# Assuming you have a 'Level' model
from project.models import Level 
# Safe content generation
def generate_safe_title():
    """Generates a unique, descriptive title using approved words."""
    approved_words = ["Beginner", "Intermediate", "Advanced", "Exploratory", "Foundational", "Introductory"]
    return f"{random.choice(approved_words)} Level {random.randint(1, 10)}"

app=create_app()
# Create dummy levels with safe content

with app.app_context(): 
    levels = Level.query.all()
    for level in levels:
        db.session.delete(level)

    for _ in range(5):  # Adjust the number of levels as needed
        level = Level(
            name=generate_safe_title(),  # Use the safe title generation function
            description="Placeholder description for a safe and inclusive level",
            tests_required=random.randint(2, 5),  # Set a random number of tests
            isUnlocked= _ == 0
            # Add other level attributes as needed, ensuring content is appropriate
        )
        db.session.add(level)

    db.session.commit()  # Commit changes to the database
