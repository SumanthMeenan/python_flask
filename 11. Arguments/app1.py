from flask import Flask, request
flask_app = Flask(__name__)

@flask_app.route('/example1')
def example1():
    sports = request.args.get("sport")
    location = request.args.get("loc")
    # climate = request.args.get("weather")
    climate = request.args['weather']
    return """<h1> We are playing {} </h1>
              <h1> We are playing in {} </h1>
              <h1> The climate is {} </h1>""".format(sports, location, climate)


# print("  hw are you ", v)
# print("hi {} hw r you".format(v))

if __name__ == "__main__":
    flask_app.run(debug=True)