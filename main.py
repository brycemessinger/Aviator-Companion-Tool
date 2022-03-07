from wsgiref.handlers import read_environ
from flask import Flask, redirect, render_template, request, flash, redirect, session, url_for
from model import Users, Trip_planner, Flight_log
import jinja2
from app import app, db
import controller
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from datetime import datetime

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "display_login"
# login_manager.login_message = ""
# login_manager.

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

now = datetime.now()
current_time = now.strftime("%H:%M")


# def getname(airport_code):
#     code_to_name = {}
#     f = open("airport codes.txt", "r")
#     for line in f.readlines():
#         locate_code = line.split(" ")[0]
#         if airport_code == locate_code:
#             words = line.split(" ")[1:]
#             return words.join(" ")
#     return "error, not found"


# landing page
@app.route("/")
def airport_finder():
    return redirect("/login")

# # results page
# @app.route("/results")
# @login_required
# def display_results():
#     return "results page"

# registration page
@app.route("/registration", methods=['GET'])
def signup_registration():
    return render_template("registration_page.html")
    
@app.route("/registration", methods=['POST'])
def submit_registration():
    
    usernames = request.form["usernames"]
    password = request.form["password"]
    enginetype = request.form["enginetypefield"]
    home_airport = request.form["homeairport"]
    
    new_user = Users(username=usernames, password=password, engine_type=enginetype, home_airport=home_airport)
    db.session.add(new_user)
    db.session.commit()

    flash(f"User {usernames} added")
    return redirect(f"/login")


# login page
@app.route("/login", methods=['GET'])
def display_login():
    return render_template("login_page.html")

@app.route("/login", methods=['POST'])
def process_login():
    usernames = request.form["usernames"]
    password = request.form["password"]

    user = Users.query.filter_by(username=usernames).first()

    if not user:
        flash("Username not found")
        return redirect("/login")
    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    login_user(user)

    flash("Logged in")
    return redirect(f"/home")


# app home page
@app.route("/home")
@login_required
def home_page():
    weather_info = controller.weather_data()
    return render_template("home_page.html",weather_info=weather_info,current_time=current_time)


# trip planner
@app.route("/trip_planner")
@login_required
def plan_trip():
    trip_planner_list = Trip_planner.query.filter_by(user_id=current_user.id).all()
    print(trip_planner_list)
    return render_template("trip_planner_page.html",trip_planner_list=trip_planner_list)

@app.route("/trip_planner", methods=["POST"])
@login_required
def log_trips():
    
    date = request.form["date"]
    refuel = request.form["refuel"]
    hours = request.form["hours"]
    miles = request.form["miles"]
    startpoint = request.form["startpoint"]
    endpoint = request.form["endpoint"]
    
    new_log = Trip_planner(date=date, refuel=refuel, hours=hours, miles=miles, startpoint=startpoint, endpoint=endpoint, user_id=current_user.id)
    db.session.add(new_log)
    db.session.commit()
    return redirect("/trip_planner")

# flight log
@app.route("/flight_log")
@login_required
def log_flights():
    flight_log_list = Flight_log.query.filter_by(user_id=current_user.id).all()
    print(flight_log_list)
    return render_template("flight_log_page.html",flight_log_list=flight_log_list)

@app.route("/flight_log", methods=['POST'])
@login_required
def log_and_display_flights():
    
    date = request.form["date"]
    enginetype = request.form["enginetype"]
    startpoint = request.form["startpoint"]
    endpoint = request.form["endpoint"]
    
    new_log = Flight_log(date=date, enginetype=enginetype, startpoint=startpoint, endpoint=endpoint, user_id=current_user.id)
    db.session.add(new_log)
    db.session.commit()
    return redirect("/flight_log")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(f"/login")