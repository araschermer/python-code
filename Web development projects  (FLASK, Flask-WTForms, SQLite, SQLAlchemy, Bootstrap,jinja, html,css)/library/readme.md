<details open="open">
  <summary><h2 style="display: inline-block"><a href="https://github.com/amgad01/python-code/tree/main/Web%20development%20projects%20%20(FLASK%2C%20Flask-WTForms%2C%20SQLite%2C%20SQLAlchemy%2C%20Bootstrap%2Cjinja%2C%20html%2Ccss)/library">Library</a></h2></summary>
    
<!-- ABOUT THE PROJECT -->
## Modules
modules used in the implementation:
* `flask ` 
* `sqlalchemy` 
* `flask_sqlalchemy`
* `requests`
* `flask_wtf`
* `wtforms`
* `flask_bootstrap`

## Example
```py
rating_choices = ["🌟", "🌟🌟", "🌟🌟🌟", "🌟🌟🌟🌟", "🌟🌟🌟🌟🌟"]
# Book form 
class BookForm(FlaskForm):
    book_name = StringField('Book Title', validators=[DataRequired()])
    author_name = StringField("Book Author", validators=[DataRequired()])
    book_rating = SelectField("Rating", choices=rating_choices,
                              validators=[DataRequired()])

    submit = SubmitField('Submit')
```
</details>

## About The Project
<br/> Coffee and wifi: a webpage that shows the books stored in a <a href="#SQLite">Sqlite</a> database using <a href="#Sqlalchemy">Sqlalchemy</a>,  with the user book title, author's name and rating of each book. This webpage project of the library  has the functionality to add, delete or edit the information of the books already stored in the database.
