# MailChimp List Helper

A simple set of tools that let you manage your pending mailchimp subscribers
(people who signed up but never confirmed their email addresses).

This is useful if you want to manually subscribe people you know wanted to sign up but didn't complete the confirmation workflow,
or if you do a lot of testing and want to clean out your lists.

This comes with both a flask web application and a command line utility.

## Installation

If you haven't already, first [setup Python, pip, and a virtualenv](https://packaging.python.org/installing/).

### Install Dependencies

`pip install -r requirements.txt`

## Running the flask app

`FLASK_APP=server.py FLASK_DEBUG=1 flask run`

Fire up [http://localhost:5000/](http://localhost:5000/) in a browser and you should see the app.

## The command line script

### Configure Mailchimp Settings

Copy the example config file locally.

`cp config.example.py config.py`

Then update the values in the file that correspond to your account information.

### Running

Just run the script and it will prompt you interactively about what you want to do.

`python mailchimp_list_manager.py `

You will have a second chance to confirm any changes before they are saved to MailChimp.


## About / Help / Extending

This app is built on [Flask](http://flask.pocoo.org/) and uses [Skeleton CSS](http://getskeleton.com/).

MailChimp calls are handled by [`python-mailchimp`](https://github.com/charlesthk/python-mailchimp).

## Disclaimer

Don't violate any MailChimp terms with this tool! I take no responsibility for anything you do with it.
