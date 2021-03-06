import os
from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from app import app
from .ASCII_Art import ascii

UPLOAD_FOLDER = os.path.dirname(__file__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER + "/static/images"
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
        file.filename = "new.jpg"
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        
        # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
        file.save(f)
        # o = os.path.join("/" + app.config['UPLOAD_FOLDER'], "out.txt")
        o = os.path.join(app.config['UPLOAD_FOLDER'], "out.txt")
        ascii(f, o)

        return redirect(url_for('show'))

    return render_template('upload.html')

@app.route('/show', methods=['GET', 'POST'])
def show():
    if request.method == 'GET':
        return render_template('show.html')