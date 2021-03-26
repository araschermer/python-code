from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route("/form", methods=["POST"])
def retrieve_form():
    name = request.form.get('username')
    password = request.form.get('password')
    return f"<h1> Name:{name} Password:{password}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
