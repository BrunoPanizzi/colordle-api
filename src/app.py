from random import seed, sample
from datetime import datetime
from flask import Flask
from flask_cors import CORS

from helpers.date_from_ISO import date_from_ISO

app = Flask(__name__)
CORS(app)

@app.route('/daily')
def daily():
  date = datetime.now().strftime('%Y-%m-%d')
  seed(date)

  sequence = sample(list(range(7)), k=4)
  
  return {
    'date': date,
    'sequence': sequence
  }

@app.route('/archive/<date>')
def archive(date):
  d = date_from_ISO(date).strftime('%Y-%m-%d')
  seed(d)

  sequence = sample(list(range(7)), k=4)
  
  return {
    'date': d,
    'sequence': sequence
  }

@app.route('/random')
def random():
  sequence = sample(list(range(7)), k=4)
  return {
    'sequence': sequence
  }

if __name__ == '__main__':
  app.run(debug=True)