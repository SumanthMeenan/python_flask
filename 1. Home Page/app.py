from flask import Flask

app = Flask(__name__)

@app.route('/') #homepage
def home():
    return "<h2> Hi! Welcome to the page </h2>" #hw much html we know that much we can play

if __name__ == "__main__":
    app.run()