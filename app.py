import datetime
import json
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from jinja2.utils import generate_lorem_ipsum
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from apscheduler.schedulers.background import BackgroundScheduler
from bson import ObjectId
from bson.json_util import dumps


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")


# work has to be done here

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(sensor, 'interval', seconds=30)
scheduler.start()

app = Flask(__name__)
app.json_encoder = JSONEncoder
auth = HTTPBasicAuth()
app.config["MONGO_URI"] = "mongodb+srv://bansalnaman:bansal@self-lkibt.mongodb.net/OwnDisaster?retryWrites=true&w=majority"
mongo = PyMongo(app)
userCol = mongo.db.users

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye"),
    "naman": generate_password_hash("bansal")
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route('/')
@auth.login_required
def hello_world():
    return ('Hello, World!'), 200


@app.route('/dedo')
def userDedo():
    users = list(userCol.find({}))
    return jsonify({"data": users}), 200

@app.route('/test1')
def loremDedo():
    return jsonify({"data": generate_lorem_ipsum()}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1502)
