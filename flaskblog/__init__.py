from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)   
app.config['SECRET_KEY'] = 'cdccefb9e9b1f59ecbb3d6e3653ac636'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes