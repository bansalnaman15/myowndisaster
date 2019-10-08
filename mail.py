from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "nanchalchadwani@gmail.com"
app.config['MAIL_PASSWORD'] = "Mayank123"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'nanchalchadwani@gmail.com', recipients = ['bansalnaman15@gmail.com'])
   msg.body = "Hello Naman"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run()
