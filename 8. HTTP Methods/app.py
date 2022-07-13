from flask import Flask, request, redirect, url_for, render_template 
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return render_template("index.html")

@flask_app.route('/login', methods = ['POST', 'GET'])
def login():
    print("request.method: " , request.method)
    if request.method == "POST":
        player = request.form['sportsman']
        return redirect(url_for('appreciate', player_name = player ))
    else:
        print("request.form: ", request.form)
        # print(request.args.get('sportsman'))
        print("request.args: ", request.args)
        # player = request.args.get('sportsman')
        # return redirect(url_for('appreciate', player_name = player ))
        return render_template("login.html")


@flask_app.route('/<player_name>')
def appreciate(player_name):
    return "Well done {}!".format(player_name) 


if __name__ == "__main__":
    flask_app.run(debug = True)