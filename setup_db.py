from app import db, app

# Create the database
with app.app_context():
    db.create_all()
