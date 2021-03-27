from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def home_page():
    return '<h1>Guess a number between 1 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>'


random_number = randint(1, 9)


@app.route("/<int:number>")
def user_input(number):
    print(random_number)
    if number > random_number:
        return "<h1>Your guess is too high<h1>" \
               '<p><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" "></img></p>'
    elif number < random_number:
        return "<h1>your guess is too low</h1>" \
               '<p><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" "></img></p>'
    else:
        return "<h1>Your guess  is perfect</h1>" \
               '<p><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" "></img</p>'


if __name__ == "__main__":
    app.run(debug=True)
