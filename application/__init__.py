from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restplus import Api

api = Api()

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)
api.init_app(app)

import routes
