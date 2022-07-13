#canonical URL

from flask import Flask 
flask_app = Flask(__name__)

@flask_app.route('/welcome')
def welcome():
    return "Welcome to Neuro Labs"

# "http://127.0.0.1:5000/welcome/ won't work"

@flask_app.route('/score/') #/score or /score/
def score():
    return "Welcome to cricket ground"

if __name__ == "__main__":
    flask_app.run(debug = True)

#same function names not allowed