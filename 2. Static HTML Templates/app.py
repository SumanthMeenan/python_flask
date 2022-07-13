from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home/') #homepage
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()



#port number 8000 - Django
#port number 5000 - Flask