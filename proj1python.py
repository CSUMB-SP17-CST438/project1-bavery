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
            "Api-Key": os.environ['Api-Key']
    }

    getty_response = requests.get(getty_url, headers=my_headers)
    json_body = getty_response.json()

    
    background_url = json_body['images'][randImg]['display_sizes'][0]['uri']

    twit= Twython(
       app_key=os.environ['app_key'],
       app_secret=os.environ['app_secret'],
       oauth_token=os.environ['oauth_token'],
       oauth_token_secret=os.environ['oauth_token_secret'])
       
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
            link = "httptwitter.com/" + quote['user']['screen_name'] + "/status/" + Id
        count = count + 1
    
    
    return render_template('proj1.html', background=background_url, quote=content, author = author, link = link)
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
