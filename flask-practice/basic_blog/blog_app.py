from flask import Flask, render_template

# This is a very simple blog using Flask, jinja2 to render basic html templates
app = Flask(__name__)
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


if __name__ == "__main__":
    app.run()
