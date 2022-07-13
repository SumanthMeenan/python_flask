from flask import Flask

app1 = Flask(__name__)

@app1.route('/home/') #rule
def website():
    return "<h2> Hi! Welcome to the page </h2>" #hw much html we know that much we can play

if __name__ == "__main__":
    app1.run()