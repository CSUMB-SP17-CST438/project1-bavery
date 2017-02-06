import flask
import os
from random import randint
from flask import render_template

app = flask.Flask(__name__)

@app.route('/random')
@app.route('/random/<num>')
def index():
  
    getty_url = \
    "https://api.gettyimages.com/v3/search/images?fields=id,title,thumb,referral_destinations&sort_order=best&phrase=space"

    my_headers = {
            "Api-Key": "nw2pc26ukj2t5ubcrps4py2r"
    }

    getty_response = requests.get(getty_url, headers=my_headers)
    json_body = getty_response.json()

    print json_body["images"][0]["display_sizes"][0]["url"]

    twitter_url = "https://api.twitter.com/1.1/account/verify_credentials.json"



    oauth = requests_oauthlib.OAuth1(

        "<API_KEY>", 

        "<API_SECRET>",

        "<ACCESS_TOKEN>",

        "<ACCESS_TOKEN_SECRET>"

    )



    response = requests.get(twitter_url, auth=oauth)

  
  
  
        x = randint(0,100)
        x = str(x)
        return render_template('proj1.html', num=x)
    
    app.run(

        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0'),
        debug=True
    )
