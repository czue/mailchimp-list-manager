from flask import Flask, render_template, url_for

app = Flask(__name__)

# url_for('static', filename='css/normalize.css')
# url_for('static', filename='css/skeleton.css')

@app.route('/')
def hello_world():
    name = 'Cory Zue'
    return render_template('home.html', name=name)

