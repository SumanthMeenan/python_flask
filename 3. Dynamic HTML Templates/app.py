from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home/') #homepage
def home():
    AGE = 20
    NAME = "Neuro Labs"

    #these values can from database
    return render_template('index.html', name = NAME, age = AGE)

if __name__ == "__main__":
    app.run()
