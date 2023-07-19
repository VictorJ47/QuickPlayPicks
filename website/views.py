#route of the application. contains routes (urls)
from flask import Blueprint, render_template

#define the name of the blueprint
#doesn't need to have the same name as the file
views = Blueprint('views', __name__)

@views.route('/')
#home function will run when this route is hit
def home():
    return render_template("home.html")