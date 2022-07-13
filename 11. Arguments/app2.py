from flask import Flask , request
flask_app = Flask(__name__)


@flask_app.route("/example2", methods = ['POST', 'GET'])
def post_function():

    if request.method == 'POST':
        game = request.form.get('sport')
        player = request.form['player']
        return '<h1> {} is playing {} </h1>'.format(player, game)

    return ''' <form method = "POST" action = '/example2'> 
                Sports <input type = "text" placeholder = "Enter Sport" name = "sport" >
                Player <input type = "text" placeholder = "Enter Player" name = 'player'> 
                <input type = "submit" >
                </form> '''

@flask_app.route("/example3", methods = ["POST"])
def json_format():
    data = request.get_json()
    player = data['player']
    sport = data['sport']
    return "{} is playing {} ".format(player, sport)

if __name__ == "__main__":
    flask_app.run(debug=True)

#login page creation, signin, signup pages - Assignment