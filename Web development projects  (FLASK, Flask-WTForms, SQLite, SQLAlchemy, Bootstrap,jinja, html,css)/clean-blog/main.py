import smtplib
from flask import Flask, render_template, request
import requests
import os

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    """ retrieves all blog posts through a request using the npoint api to retrieve the data from a given npoint page"""
    posts = requests.get("https://api.npoint.io/0067e63917ca7a5034d9").json()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    posts = get_all_posts()
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    # when a message is submitted (post request)
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        send_email(username, email, phone, message)
        return render_template("contact.html", message="Message sent ✔️")
    # Otherwise renders the contact page "
    return render_template("contact.html", message="Contact Me")


def send_email(name, email, phone, message):
    """sends an email automatically with a name, email, phone  number and a message"""
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
