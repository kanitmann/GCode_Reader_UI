import sys,os,re   
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from config import *

app=Flask(__name__)
app.secret_key = app_key

if not os.path.isdir(upload_dest):
    os.mkdir(upload_dest)

app.config['MAX_CONTENT_LENGTH'] = file_mb_max * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

## on page '/upload' load display the upload file
@app.route('/upload')
def upload_form():
    return render_template('Upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':    
        if 'files[]' not in request.files:
            flash('No files found, try again.')
            return redirect(request.url)    
        else:
            files = request.files.getlist('files[]')    
            for file in files:
                if file and allowed_file(file.filename):
                    file.save(os.path.join( upload_dest, file.filename))    
                    flash('File(s) uploaded')
    return redirect('/upload')

#############################
# Additional Code Goes Here #
#############################

if __name__ == "__main__":
    print('to upload files navigate to http://127.0.0.1:4000/upload')
    app.run(port=4000,debug=True,threaded=True)