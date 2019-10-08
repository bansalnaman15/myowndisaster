from flask import Flask
from flask_mail import Mail, Message

from app import loremDedo

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "namanash2015@gmail.com"
app.config['MAIL_PASSWORD'] = "Naman2015"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.route("/")
def home():
   return "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

@app.route("/mail")
def index():
   msg = Message('Hello', sender = 'namanash2015@gmail.com', recipients = ['bansalnaman15@gmail.com'])
   msg.body = "Hello Naman"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run()
