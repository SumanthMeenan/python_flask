from flask import Flask 
flask_app = Flask(__name__)

@flask_app.route('/')
def home_page():
    return "Welcome to Flask"

if __name__ == "__main__":
    flask_app.run(debug = True)