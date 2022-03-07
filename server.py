from main import app
from model import connect_to_db
from sqlalchemy import func
from model import Users, Trip_planner, Flight_log, connect_to_db, db

def load_users(user_filename)
    """load users from Users.user into db."""
    
    for i, row in enumerate(open(user_filename)):
        row = row.rstrip()
        user_id, username, password, engine_type, home_airport = row.split("|")

        user = User()

    db.session.add(user)