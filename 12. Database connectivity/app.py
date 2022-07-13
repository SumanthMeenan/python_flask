from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_mysqldb import MySQL 
from forms import RegistrationForm, LoginForm 
import yaml

app = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods= ["GET", "POST"])
def index():
    if request.method == "POST":
        userDetails = request.form 
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        # return "SUCCESS" 
        return redirect('/users')
    return render_template("index.html") 

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM users")
    if result > 0:
    userdetails = cur.fetchall()
    return render_template('users.html', users = userdetails)

if __name__ == "__main__":
    app.run(debug = True)
