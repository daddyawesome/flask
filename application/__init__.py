from flask import Flask
from config import Config
<<<<<<< HEAD
from flask_mongoengine = MongoEngine
=======
from flask_mongoengine import MongoEngine
>>>>>>> 5f574d10d7615ed12010d1590f60a5b3de583ec2

app = Flask(__name__)
app.config.from_object(Config)

<<<<<<< HEAD
db = MongoEngine
=======
db = MongoEngine()
db.init_app(app)
>>>>>>> 5f574d10d7615ed12010d1590f60a5b3de583ec2

from application import routes

