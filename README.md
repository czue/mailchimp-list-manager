# mailchimp-list-manager

This simple command line tool will let you manage your pending mailchimp subscribers
(people who signed up but never confirmed their email addresses).

It's useful if you want to manually subscribe people you know wanted to sign up but didn't complete the confirmation workflow,
or if you do a lot of testing and want to clean out your lists.

## Setup

### Install Dependencies

`pip install -r requirements.txt`

### Configure Mailchimp Settings

Copy the example config file locally.

`cp config.example.py config.py`

Then update the values in the file that correspond to your account information.

## Running

Just run the script and it will prompt you interactively about what you want to do.
You will have a second chance to confirm any changes before they are saved to Mailchimp.


## Help / Extending

To modify or extend this tool, it is recommended to read/refer to the API docs for `[python-mailchimp](https://github.com/charlesthk/python-mailchimp)`.
