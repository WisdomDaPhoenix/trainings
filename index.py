from flask import Flask, render_template, request, url_for, send_from_directory
from flask_mail import Mail, Message
import json

with open('clientsdata/clients.json', 'r') as file:
    content = json.load(file)

app = Flask(__name__)

app.config['MAIL_SERVER'] = "mail.dmarketforces.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "wisdom.enefiok@dmarketforces.com"
app.config['MAIL_PASSWORD'] = "12Hallmark1!"
app.config['MAIL_DEFAULT_SENDER']=('DXY-Trainings','wisdom.enefiok@dmarketforces.com')
app.config['SECRET_KEY'] = "bossDatron24"

mail = Mail(app)


@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submitData():
    open("clientsdata/clients.json").close()

    name = request.form['name']
    course = request.form['course']
    phone = request.form['phone']
    email = request.form['email']

    d = {"Name": name,
         "Course": course,
         "Phone": phone,
         "Email": email}

    with open('clientsdata/clients.json','w') as file:
        content["data"].append(d)
        json.dump(content, file)

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

@app.route("/courses",methods=["GET"])
def courses():
    try:
        return send_from_directory('static','TRAINING BROCHURE.pdf')
    except FileNotFoundError as f:
        return f"Courses not available: {f}"


if __name__ == "__main__":
     app.run(port=5200,debug=True,host="0.0.0.0")


                  
