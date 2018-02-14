import os
from flask import Flask, render_template, request, send_from_directory
from app import app

UPLOAD_FOLDER = os.path.dirname(__file__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index')
def index():
    #user = {'nickname': 'there'}  # fake user
    return render_template('index.html',
                           title='Home')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        f = os.path.join("/" + app.config['UPLOAD_FOLDER'], file.filename)
        
        # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
        file.save(f)
        
        return render_template('show.html',
                           title='Home')

    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
