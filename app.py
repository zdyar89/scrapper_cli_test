from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/redditDaily')
def reddit_daily():
    return 'Reddit daily tickers page'

@app.route('/redditWeekly')
def reddit_weekly():
    return 'Reddit weekly tickers page'

@app.route('/marketVitals')
def market_vitals():
    return 'Market vital signs page'