Django IG
==========

Photo sharing social media site built with Python/Django. Based on Instagram's design. The server also uses Django Channels to establish a websocket connection to the client for messages and soon, notifications.

## Installation

Install dependencies

    pip install -r requirements.txt

Run these two commands in two separate terminals

    python3 manage.py runserver --noworker
    python3 manage.py runworker
