import json
from flask import Flask, render_template, request, Response
from mailchimp3 import MailChimp
import config

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = 'Cory Zue'
    return render_template('home.html', name=name)


@app.route('/api/lists/', methods=['POST'])
def get_lists():
    client = _get_mailchimp_client()
    lists = client.lists.all(get_all=True, fields="lists.name,lists.id")
    return Response(json.dumps(lists), mimetype='application/json')


def _get_mailchimp_client():
    username = request.form['username'] or config.MAILCHIMP_USERNAME
    api_key = request.form['api-key'] or config.MAILCHIMP_SECRET_KEY
    return MailChimp(username, api_key)
