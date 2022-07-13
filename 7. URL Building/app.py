from flask import Flask, redirect, url_for
flask_app = Flask(__name__)

@flask_app.route('/organizer')
def event():
    return "Welcome Event Organizer"

@flask_app.route('/player/<player_name>')
def football(player_name):
    return "Welcome {} to the world football championship".format(player_name)

@flask_app.route('/audience/<person_name>')
def audience(person_name):
    if person_name == "organizer":
        return redirect( url_for('event') )
    else:
        return redirect( url_for('football', player_name = person_name) )

if __name__ == "__main__":
    flask_app.run(debug = True)