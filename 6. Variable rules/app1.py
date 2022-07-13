from flask import Flask 
flask_app = Flask(__name__)

@flask_app.route('/welcome/<int:score>')
def cricket(score):
    print("Type of firstname variable is: {}".format(type(score)))
    return "Dravid scored {} in test match. ".format(score)

if __name__ == "__main__":
    flask_app.run(debug = True)