from flask import Flask, request, render_template,flash, redirect, url_for
from smtplib import SMTP
from dotenv import load_dotenv; load_dotenv()
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


projects = [
        {
            'title': 'Project 1',
            'description': 'Short description of Project 1.',
            'image': './static/IMG_8858.jpg',
            'link': 'link-to-project1'
        },
        {
            'title': 'Project 2',
            'description': 'Short description of Project 2.',
            'image': './static/IMG_8858.jpg',
            'link': 'link-to-project2'
        },
        {
            'title': 'Project 3',
            'description': 'Short description of Project 3.',
            'image': './static/IMG_8858.jpg',
            'link': 'link-to-project3'
        }
    ]

@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        try:
            send_mail(**request.form)
            flash("Thank you for the message. I will aim to respond within 24hours",'info')
            return redirect('/#contact')
        except TypeError:
            flash("Message Not Sent (Error 500). Please Ensure all fields are complete",'error')
            return redirect(url_for('home'))
    return render_template('index.html',projects=projects)


def send_mail(name,email,message):
    with SMTP("smtp.gmail.com",587) as connection:
        my_email = "daniel.a.fadele@gmail.com"
        msg = f"Subject:App Message \n\nName: {name} \nContact Email: {email}, \n\nMessage: {message}"
        connection.starttls() # transport layer security
        connection.login(my_email,os.getenv("APP_PASSWORD"))
        connection.sendmail(my_email,my_email,msg)





if __name__=='__main__':
    app.run(debug=True)