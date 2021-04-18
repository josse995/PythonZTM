from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<username>')
def username_page(username=None):
    return render_template('index.html', name=username)

    
@app.route('/<username>/<int:post_id>')
def username_page_post(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)