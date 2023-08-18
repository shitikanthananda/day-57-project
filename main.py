from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url).json()
post_objects = []
for i in response:
    post_obj = Post(i["id"], i["title"], i["subtitle"], i["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog=post_objects)


@app.route('/post/<int:num>')
def blog(num):
    requested_post = None
    for obj in post_objects:
        if obj.id == num:
            requested_post = obj
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
