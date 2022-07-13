from flask import Flask, render_template, request, url_for, redirect 
from werkzeug.utils import secure_filename 
flask_app = Flask(__name__)

# flask_app.config['UPLOAD_FOLDER'] = '/home/'

@flask_app.route('/file_uploader')
def file_uploader():
    return render_template('index.html')

@flask_app.route('/call', methods = ['GET', 'POST'])
def call():
    if request.method == 'POST':
        file1 = request.files['file']
        file1.save(secure_filename(file1.filename))
        return "{} uploaded successfully".format(file1.filename)

if __name__ == "__main__":
    flask_app.run(debug = True)
