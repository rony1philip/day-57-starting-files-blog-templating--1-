from flask import Flask, render_template
from post import Post

post = Post()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = post.all_posts, ids = post.ids)

@app.route('/post/<id>')
def blog_post(id):
    index = int(id) - 1
    return render_template("post.html",body = post.all_posts[index]['body'], title = post.all_posts[index]['title'], subtitle = post.all_posts[index]['subtitle'])

if __name__ == "__main__":
    app.run(debug=True)
