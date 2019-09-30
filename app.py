import datetime
import json
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from apscheduler.schedulers.background import BackgroundScheduler
from bson import ObjectId
from bson.json_util import dumps


# class JSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         if isinstance(o, datetime):
#             return str(o)
#         return json.JSONEncoder.default(self, o)

def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")
    user=userCol.find_one({"name":"Naman"})
    print(user)
    if "online" in user.keys():
        if (user["online"]==True):
            user["online"]=False
        else: user["online"]=True
    else: user["online"]=True
    userCol.update_one({"name":"Naman"},{"$set":user})
scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(sensor, 'interval', seconds=30)
scheduler.start()

app = Flask(__name__)
# app.json_encoder = JSONEncoder
auth = HTTPBasicAuth()
users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye"),
    "naman":generate_password_hash("bansal")
}


app.config["MONGO_URI"] = "mongodb+srv://bansalnaman:bansal@self-lkibt.mongodb.net/OwnDisaster?retryWrites=true&w=majority"
mongo = PyMongo(app)
userCol = mongo.db.users

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

@app.route('/')
@auth.login_required
def hello_world():
    return ('Hello, World!'),200

@app.route('/dedo')
def userDedo():
    users = list(userCol.find({}))
    return jsonify({"data":users}),200


if __name__ == '__main__':
    app.run()