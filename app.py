import datetime
import json
from flask import Flask, jsonify, request
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

@app.route('/naman')
@auth.login_required
def kuchbhidedo():
    a="The term brother comes from the Proto-Indo-European *bʰréh₂tēr, which becomes Latin frater, of the same meaning. Sibling warmth, or sibling affect between male siblings has been correlated to some more negative effects. In pairs of brothers higher sibling warmth is related to more risk taking behaviour although risk taking behaviour is not related to sibling warmth in any other type of sibling pair. The cause of this phenomenon in which sibling warmth is only correlated with risk taking behaviours in brother pairs still is unclear. This finding does, however, suggest that although sibling conflict is a risk factor for risk taking behaviour, sibling warmth does not serve as a protective factor.[4] Some studies suggest that girls having an older brother delays the onset of menarche by roughly one year.[5] Research also suggests that the likelihood of being gay increases with the more older brothers a man has.[6] Some analyzers have suggested that a man's attractiveness to a heterosexual woman may increase with the more he resembles her brother, while his unattractiveness may increase the more his likeness diverges from her brother.[7] Females with a twin or very close-in-age brother, sometimes view him as their male alter ego, or what they would have been like, if they had a Y chromosomes."
    return a

@app.route('/namandedo',methods=["POST"])
def lolololol():
    data = request.get_json()
    return jsonify(data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1502)
