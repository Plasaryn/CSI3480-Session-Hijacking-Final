from flask import Blueprint, render_template, request, redirect, make_response
from users import is_valid_login
from session import Session, SessionExpired

views = Blueprint(__name__, "views")

@views.route("/")
def index():
    return render_template("home.html")

@views.route("/home")
def home():
    return index()
  
@views.route("/profile")
def profile():
  session_id = request.cookies.get("session_id")
  if not session_id:
     return redirect("/login")
  try:
     user_data = Session.get_session_info(session_id)
  except SessionExpired:
     return redirect("/logout")
  return render_template("profile.html", **user_data)

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
      resp = make_response(redirect("/profile"))
      resp.set_cookie(
           'session_id',
           Session.new(request.form['username']).secret_session_id
        )
      return resp
    else:
      error = 'Invalid username/password'
      return render_template('login.html', error=error)
  else:
    return render_template("login.html", error=None)
  
@views.route("/logout")
def logout():
   resp = redirect("/")
   resp.set_cookie('session_id', '', expires=0)
   return resp