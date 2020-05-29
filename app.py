from flask import render_template,redirect,flash,request,abort,url_for
from myproject import app,db

from flask_login import login_user,login_required,logout_user

from myproject.models import User

from myproject.forms import LoginForm,RegistrationForm

from werkzeug.security import generate_password_hash,check_password_hash

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out")
    return redirect(url_for('index'))

@app.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        try:
            if check_password_hash(user.password_hash,form.password.data) and user is not None:
               login_user(user)
               flash("You logged in successfully")
               next = request.args.get('next')
               if next == None or not next[0] == '/':
                  next = url_for('index')
               return redirect(next)
        except AttributeError:
            redirect(url_for('login'))
    return render_template('login.html',form=form)


@app.route('/Register',methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        passwd = form.password.data
        user = User(username,passwd)
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registration")
        return redirect(url_for('login'))

    return render_template('register.html',form=form)