from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'jlkfd!@jgkld$FR*CDSwsR$^Y'
Bootstrap(app)

# configure sqlalchemy
# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
# to silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

rating_choices = ["🌟", "🌟🌟", "🌟🌟🌟", "🌟🌟🌟🌟", "🌟🌟🌟🌟🌟"]


class BookForm(FlaskForm):
    book_name = StringField('Book Title', validators=[DataRequired()])
    author_name = StringField("Book Author", validators=[DataRequired()])
    book_rating = SelectField("Rating", choices=rating_choices,
                              validators=[DataRequired()])

    submit = SubmitField('Submit')


@app.route('/')
def home():
    all_books = db.session.query(Book).all()

    return render_template("index.html", books=all_books)


@app.route('/add', methods=["GET", "POST"])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        new_book = Book(title=book_form.book_name.data, author=book_form.author_name.data,
                        rating=book_form.book_rating.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=book_form)


# TO edit stored entries :

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        book_to_update.author = request.form["author"]
        book_to_update.title = request.form["title"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
