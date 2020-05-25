import tweepy
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

access_token = '1132949867666366464-dCkTWOLUEnGnhPpBeJwxGbduhmo8Wp'
access_token_secret = 'a2GhNcIBLRtkrd3GpjFdW4sOtLT5OhsJnz0MKUhQHCRW9'
consumer_key = 'OHfGmAhpDjQty43pB1XYRMcme'
consumer_secret = 'lcUid3EIozytlnmr6UD8vQMAIUYzP8Ur2hCBnlCkOVRwN3tJ25'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def fetch(id, number=1): 
    try: 
      for tweet in api.user_timeline(id=id, count=number): 
          return tweet.text
    except:
      return "There's something wrong with the username inputted."

tweet = ""
user = None

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST': 
      global user
      user = request.form["username"]
      global tweet
      tweet = fetch(user)
      return redirect(url_for("test"))
  else: 
    return render_template("index.html")

@app.route('/test', methods=['GET', 'POST'])
def test(): 
    global tweet
    if not tweet: 
      tweet = "Error!"
    return render_template("test.html", twt=tweet, user=user)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 