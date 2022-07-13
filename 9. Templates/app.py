from flask import Flask, request, redirect, url_for, render_template 
flask_app = Flask(__name__)

@flask_app.route('/matchresult')
def score():
    record = {'sachin':34, 'dhoni':55, 'kohli':48}
    return render_template('index.html', match = record)

if __name__ == "__main__":
    flask_app.run(debug = True)