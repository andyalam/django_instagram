Django IG
==========

![alt tag](https://raw.githubusercontent.com/andyalam/django_ig/master/demo_screenshot.png)

Photo sharing social media site built with Python/Django. Based on Instagram's design. The server also uses Django Channels to establish a websocket connection to the client for messages and soon, notifications.
Channels requires a redis server to be running, more info can be found about Django Channels [here](https://channels.readthedocs.io/en/stable/)

## Installation

Install dependencies

    pip3 install -r requirements.txt

Ensure that [Redis](http://redis.io/) is installed and running on port 6379 (default).

Run these two commands in two separate terminals

    python3 manage.py runserver --noworker
    python3 manage.py runworker
