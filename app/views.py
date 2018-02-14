import os
from flask import Flask, render_template, request
from app import app

UPLOAD_FOLDER = os.path.basename('tmp')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index')
def index():
    #user = {'nickname': 'there'}  # fake user
    return render_template('index.html',
                           title='Home')

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        file = request.files['image']
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        
        # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
        file.save(f)
        
        return render_template('index.html',
                           title='Home')

    return render_template('upload.html')