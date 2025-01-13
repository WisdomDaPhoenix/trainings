from flask import Flask, render_template, request, url_for
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER'] = "mail.dmarketforces.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "wisdom.enefiok@dmarketforces.com"
app.config['MAIL_PASSWORD'] = "12Hallmark1!"
app.config['MAIL_DEFAULT_SENDER']=('DMarketForces','wisdom.enefiok@dmarketforces.com')

mail = Mail(app)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submitData():
    name = request.form['name']
    course = request.form['course']
    email = request.form['email']
    subject = f"Acknowledgement of Course Registration"
    
    mailbody = f"""Thank you {name} for registering your interest in our training course \n\n 
                   Course Name: {course} \n\n
                   Our courses run 3 times a week \n\n
                   Time: 10.00am \n\n
                   You will be contacted shortly for any further information"""
    successmsg = f"Thanks for your interest! We have sent an acknowledgement email to {email}"
    try:
        msg = Message(subject, recipients=[email])
        msg.body = mailbody
        mail.send(msg)
        return render_template("success.html", successmsg=successmsg)
    except Exception as e:
        return f"Send failure: {e}"




if __name__ == "__main__":
     app.run(port=5200,debug=True,host="0.0.0.0")


                  
