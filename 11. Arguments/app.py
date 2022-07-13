from flask import Flask, request
flask_app = Flask(__name__)

@flask_app.route('/example1')
def example1():
    sports = request.args.get("sport")
    return "<h1> We are playing {} </h1>".format(sports)

#GET - To query
#POST - To upload the data

if __name__ == "__main__":
    flask_app.run(debug=True)