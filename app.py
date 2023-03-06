from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RegisterForm, LoginForm, ContactForm
from flask_login import login_required, current_user, LoginManager, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import db, User
from datetime import datetime
from quit import QuitTracker
from controller import send_message
import json
from random import randint
app = Flask(__name__)

app.config.from_pyfile("config.py")

db.init_app(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/', methods=["GET","POST"])
def index():
    tracker = None
    form=ContactForm()
    if request.method=="POST":
        send_message(request.form.get("name"),
                     request.form.get("email"),
                     request.form.get("subject"),
                     request.form.get("text")
                     )
        return redirect(url_for("index"))
    else:
        _id = current_user.get_id()
        if _id:
            requested_user = User.query.get(_id)
            form = ContactForm(name=requested_user.name,
                               email=requested_user.email)
            tracker = QuitTracker(requested_user.years_of_smoking,
                                requested_user.date,
                                requested_user.time,
                                requested_user.smoked_cigarettes_per_day,
                                requested_user.cigarettes_in_pack,
                                requested_user.price,
                                requested_user.currency)
            return render_template('index.html', tracker=tracker, form=form)
        return render_template("index.html", tracker=tracker, form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        if User.query.filter_by(email=form.email.data).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))
        else:
            name = request.form.get("name")
            email = request.form.get("email")
            password = generate_password_hash(request.form.get("password"))
            smoked_cigarettes_per_day = request.form.get(
                "smoked_cigarettes_per_day")
            cigarettes_in_pack = request.form.get("cigarettes_in_pack")
            years_of_smoking = request.form.get("years_of_smoking")
            date = request.form.get("date")
            time = request.form.get("time")
            price = request.form.get("price")
            currency = request.form.get("currency").split()[1]
            new_user = User(name=name,
                            email=email,
                            password=password,
                            smoked_cigarettes_per_day=smoked_cigarettes_per_day,
                            cigarettes_in_pack=cigarettes_in_pack,
                            years_of_smoking=years_of_smoking,
                            date=date,
                            time=time,
                            price=price,
                            currency=currency)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))
    else:
        return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('index'))
    return render_template("login.html", form=form)


@app.route("/edit-stats/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    if request.method == "POST":
        user = User.query.get(id)
        user.smoked_cigarettes_per_day=request.form.get("smoked_cigarettes_per_day")
        user.years_of_smoking=request.form.get("years_of_smoking")
        user.date=request.form.get("date")
        user.time=request.form.get("time")
        user.price=request.form.get("price")
        user.currency=request.form.get("currency")
        db.session.commit()
        return redirect(url_for("index"))
    if current_user.get_id() == str(id):
        is_edit = True
        user = User.query.get(id)
        edit_form = RegisterForm(smoked_cigarettes_per_day=user.smoked_cigarettes_per_day,
                                 cigarettes_in_pack=user.cigarettes_in_pack,
                                 years_of_smoking=user.years_of_smoking,
                                 price=user.price,
                                 currency=user.currency
                                 )
        return render_template("register.html", form=edit_form, is_edit=is_edit, date=user.date, time=user.time)
    else:
        return render_template("404.html"), 404
    


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.errorhandler(404)
def bad_request(e):
    return render_template("404.html")


@app.context_processor
def copyright():
    return {"year": datetime.now().year}

@app.context_processor
def quote():
    num = randint(1, 60)
    with open("./quotes.json", "r") as f:
        data = json.load(f)
    return {"quote": data[str(num)]}




if __name__ == '__main__':
    app.run()
