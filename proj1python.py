import flask
import os
from random import randint
from flask import render_template
from twython import Twython
import json
import requests
import requests_oauthlib

app = flask.Flask(__name__)

@app.route('/')
def index():
    
    randImg = randint(0,30)
    randTweet = randint(0,75)
  
    getty_url = \
    "https://api.gettyimages.com/v3/search/images?fields=comp,id,title,thumb,referral_destinations&sort_order=best&phrase=space"

    my_headers = {
            "Api-Key": "nw2pc26ukj2t5ubcrps4py2r"
    }

    getty_response = requests.get(getty_url, headers=my_headers)
    json_body = getty_response.json()

    
    background_url = json_body["images"][randImg]["display_sizes"][0]["uri"]

    twit= Twython(
       app_key="twmzdajx4canLqONUCRrXutQF",
       app_secret="ebeQ8qYSNhZU5aRDrVBx9Z54Rvsvy3XtrQsN1SPEaH3a70mikn",
       oauth_token="827281167871127553-OlX7qaPFv027RXn247BGwfKag3OLz4I",
       oauth_token_secret="fmzXPa03DFN3NSpTeTV38vDr2NzZAzttkJkcc2EPTb03E")
       
    tweets = twit.search(q= 'In space, no one can', count = 150)
    quotes = tweets['statuses']
    count = 0
    content = ""
    author = ""
    link = ""
    for quote in quotes:
        if count == randTweet:
            content = quote['text']
            author = "@" + quote['user']['screen_name']
            Id = quote['id_str']
            link = "http://www.twitter.com/" + quote['user']['screen_name'] + "/status/" + Id
        count = count + 1
    
    
    return render_template('proj1.html', background=background_url, quote=content, author = author, link = link)
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
