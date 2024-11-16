from flask import Blueprint, render_template, request, redirect, make_response
from login import is_valid_login

views = Blueprint(__name__, "views")

@views.route("/")
def index():
    return render_template("home.html")

@views.route("/home")
def home():
    return index()
  
@views.route("/profile")
@views.route("/profile/<name>")
def profile(name=None):
  username = request.cookies.get("username")
  if not (username):
        return redirect("/login")
  elif username != name:
     return redirect(f"/profile/{username}")
  else:
    return render_template("profile.html", pname=name.capitalize())

@views.route("/login", methods=["GET", "POST"])
def login():
  username = request.cookies.get("username")
  if username:
     return redirect(f"/profile/{username}")
  if request.method == "POST":
    if is_valid_login(
       request.form['username'],
       request.form['password']):
       """True Codeblock"""
       resp = make_response(redirect(f"/profile/{request.form['username']}"))
       resp.set_cookie('username', request.form['username'])
       return resp
    else:
       error = 'Invalid username/password'
       return render_template('login.html', error=error)
  else:
    return render_template("login.html", error=None)
  
@views.route("/logout")
def logout():
   resp = redirect("/")
   resp.set_cookie('username', '', expires=0)
   return resp