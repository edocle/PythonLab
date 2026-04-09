
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = '1271d528f59507ac140fc8e008c8d18cad39e0e2d9a31d31'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from myapp import routes, models