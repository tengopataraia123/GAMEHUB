from flask import Blueprint, render_template,redirect,url_for,flash
from myproject import db,active_users
from myproject.models import Gamer
from myproject.auth.forms import LoginForm, RegistrationForm
from flask_login import login_user

auth_blueprint = Blueprint('auth', __name__, template_folder='templates/auth')

@auth_blueprint.route("/auth",methods=["GET","POST"])
def auth():
    global active_users

    registrationForm = RegistrationForm()
    loginForm = LoginForm()

    if registrationForm.validate_on_submit():
        registrationForm.check_email(registrationForm.email.data)
        registrationForm.check_username(registrationForm.username.data)
        gamer = Gamer(name=registrationForm.username.data,
                        email=registrationForm.email.data,
                        password=registrationForm.password.data)
        gamer.photo = "/avatars/Ninja.jpg"
        print(registrationForm.email.data,registrationForm.username.data,registrationForm.password.data)
        db.session.add(gamer)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('auth.auth'))
    if loginForm.validate_on_submit():
        gamer = Gamer.query.filter_by(email = loginForm.email.data).first() or Gamer.query.filter_by(name = loginForm.email.data).first()
        if gamer and gamer.check_password(loginForm.password.data) is not None:
            login_user(gamer)
            active_users.append(gamer.id)
            flash('Log in Success!')
            return redirect(url_for("index.index"))
    return render_template('auth.html', regForm=registrationForm,loginForm=loginForm)