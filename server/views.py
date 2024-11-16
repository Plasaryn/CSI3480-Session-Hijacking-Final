from flask import Blueprint, render_template, url_for, request

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/home")
def home_():
    return url_for("/")

@views.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    return
  else:
    return render_template("login.html")