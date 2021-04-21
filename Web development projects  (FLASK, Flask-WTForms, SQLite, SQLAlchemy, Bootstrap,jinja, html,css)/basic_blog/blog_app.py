from flask import Flask, render_template, request
from forms import SignUpForm

# This is a very simple blog using Flask, jinja2 to render basic html templates
app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRETKEY"

blog_content = [{"title": "How to Have a Healthier and More Productive Home Office", "content": "Some content"},
                {"title": " How To Change Your Life For The Better – 33 Things You Can Do", "content": "Some content "},
                {"title": "10 Step To Successfully Outsourcing Your Online Business", "content": "Some content "},
                {"title": "“21 Ways to Dominate Youtube: The Ultimate Guide", "content": "Some content "},
                {"title": "15 Website Content Hacks A-List Bloggers Use To Create Viral Content",
                 "content": "Some content "}]

interests = ["sports", "art", "traveling"]


@app.route('/')
def home():
    return render_template("blog.html", posts=blog_content, interests=interests)


@app.route("/signup", methods=["POST","GET"])
def signup():
    signup_form = SignUpForm()
    if signup_form.is_submitted():
        user = request.form
        # to slice the indices of user returned form
        app.jinja_env.add_extension('jinja2.ext.loopcontrols')
        return render_template("user.html", user_dict=user)
    return render_template("signup.html", form=signup_form)


if __name__ == "__main__":
    app.run(debug=True)
