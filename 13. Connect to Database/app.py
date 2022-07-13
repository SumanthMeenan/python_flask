from flask import Flask, render_template, request, redirect
flask_app = Flask(__name__)
from flask_mysqldb import MySQL
import yaml

mysql = MySQL(flask_app)

db_params = yaml.load(open('params.yaml')) #graphiql
flask_app.config['MYSQL_HOST'] = db_params['mysql_host']
flask_app.config['MYSQL_USER'] = db_params['mysql_user']
flask_app.config['MYSQL_PASSWORD'] = db_params['mysql_password']
flask_app.config['MYSQL_DB'] = db_params['mysql_db']


@flask_app.route('/')
def db_connectivity():
    if request.method == 'POST':
        user_details = request.form
        name = user_details['person']
        email = user_details['mail']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/data')
    return render_template("index.html")


@flask_app.route('/data')
def users_data():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM users")
    if users > 0:
        users_details = cur.fetchall()
        return render_template('users_data.html', users = users_details)

if __name__ == '__main__':
    flask_app.run(debug = True)