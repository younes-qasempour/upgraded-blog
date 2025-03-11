from flask import Flask, render_template
import requests


posts = requests.get("https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/"
                     "fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():  # put application's code here
    return render_template('index.html', all_posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
