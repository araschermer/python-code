from flask import Flask

app = Flask(__name__)
print(__name__)


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p> This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif"width=25% >' \
           '<img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.zastavki.com%2Fpictures' \
           '%2Foriginals%2F2013%2FAnimals_Cats_Sleeping_gray_kitten_036760_.jpg&f=1&nofb=1" width=25%> '


@app.route("/bye")
def say_bye():
    """accessible on http://127.0.0.1:5000/bye"""
    return "<b><em><u>Bye!</u></em></b>"


# the same functionality, but this time using decorators in the following lines of code
def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}</em>'

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


# how to parse a url:
# The text between <> must be the same as the func parameter
# otherwise it'll throw an exception
@app.route("/<name>/<int:number>")
def greet(name, number):
    return "Hello, " + name.title() + "!\n" + f"Y{number}"


if __name__ == "__main__":
    app.run(debug=True)
