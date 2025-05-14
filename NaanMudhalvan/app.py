from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        business_name = request.form['business_name']
        owner = request.form['owner']
        zone = request.form['zone']
        document = request.files['document']
        if document:
            path = os.path.join(app.config['UPLOAD_FOLDER'], document.filename)
            document.save(path)
        return render_template('result.html', business=business_name, zone=zone)
    return render_template('apply.html')

@app.route('/admin')
def admin():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('admin.html', files=files)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

    
