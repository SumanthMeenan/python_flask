from flask import Flask 
flask_app = Flask(__name__)

@flask_app.route('/welcome/<float:avg>')
def cricket(avg):
    print("Type of firstname variable is: {}".format(type(avg)))
    return "Dravid average is {} in test match. ".format(avg)

if __name__ == "__main__":
    flask_app.run(debug = True)