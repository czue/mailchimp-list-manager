import json
from flask import Flask, render_template, request, Response
from mailchimp3 import MailChimp
import config

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html', api_key=config.MAILCHIMP_SECRET_KEY)


@app.route('/api/lists/', methods=['POST'])
def get_lists():
    client = _get_mailchimp_client()
    lists = client.lists.all(get_all=True, fields="lists.name,lists.id")
    return Response(json.dumps(lists), mimetype='application/json')


@app.route('/api/members/', methods=['POST'])
def get_members():
    client = _get_mailchimp_client()
    list_id = request.form['list']
    members = client.lists.members.all(list_id, get_all=True, status='pending',
                                       fields="members.email_address,members.id,members.timestamp_signup,members.status")
    return Response(json.dumps(members), mimetype='application/json')


def _get_mailchimp_client():
    username = ''
    api_key = request.form['api-key'] or config.MAILCHIMP_SECRET_KEY
    return MailChimp(username, api_key)
