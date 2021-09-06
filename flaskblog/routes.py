from flask import render_template, url_for, flash, redirect
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app

posts = [
    {
        'author':'Sam',
        'title':'Blog Post 1',
        'content':'blablabla',
        'date_posted': 'Jun 23 2029'
    },
    {
        'author':'Brad',
        'title':'Blog Post 2',
        'content':'blablabla',
        'date_posted': 'Jun 23 2029'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created sucssesfuly for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been loggen in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login umsuccesful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)