from flask import Flask 
flask_app = Flask(__name__)

@flask_app.route('/welcome/<firstname>')
def home_page(firstname):
    print("Type of firstname variable is: {}".format(type(firstname)))
    return "Welcome to {}".format(firstname)

if __name__ == "__main__":
    flask_app.run(debug = True)

# Assignment1: create 4 boxes which takes input from user, based on firstname, display output?