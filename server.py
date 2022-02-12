"""Module os"""
import os

from flask import (Flask,request,render_template,redirect, send_file,send_from_directory)

from flask_wtf.csrf import CSRFProtect

from s3 import (upload_file,download_file,list_file)

from resize import resize

app = Flask(__name__)
#csrf = CSRFProtect()
#csrf.init_app(app) # Compliant

UPLOAD_FOLDER = "uploads"
BUCKET = "ovasbucker"

@app.route("/")
def home():
    "Function home"
    contents = list_file("ovasbucker")
    return render_template('index.html', contents=contents)


@app.route('/upload', methods=['POST'])
def upload():
    "Function upload"
    if request.method == "POST":
        file_array = request.files.getlist('file')
        for file in  file_array :
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            resize(f"uploads/{file.filename}")
            upload_file(f"uploads/{file.filename}", BUCKET,file.filename)
    return redirect("/")

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    "Function download"
    if request.method == 'GET':
        output = download_file(filename, BUCKET)
    return send_file(output, as_attachment=True)
    

if __name__ == "__main__":
    app.run(debug=True,host="localhost",port="5000")