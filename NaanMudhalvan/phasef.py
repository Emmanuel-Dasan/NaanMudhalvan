from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Mock AI verification function
def verify_document_ai(filepath):
    # You can replace this logic with actual AI model inference
    return {
        'verified': True,
        'remarks': 'Document passed all verification checks.'
    }

@app.route('/submit_application', methods=['POST'])
def submit_application():
    if 'document' not in request.files:
        return jsonify({'error': 'No document uploaded'}), 400

    file = request.files['document']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    result = verify_document_ai(file_path)

    return jsonify({'status': 'success', 'result': result})

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
