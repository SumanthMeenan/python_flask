from flask import Flask 
flask_app = Flask(__name__)

@flask_app.route('/welcome')
def home_page():
    return "Welcome to Flask"

# @flask_app.route('/page')
def newpage():
    return "Welcome to New Page"
flask_app.add_url_rule('/page', 'page',newpage)

if __name__ == "__main__":
    flask_app.run(debug = True)