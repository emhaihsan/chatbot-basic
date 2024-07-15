import os
from flask import Flask, request, render_template, redirect, url_for, jsonify
from chatbot import chatbot_response

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('message')
    response = chatbot_response(user_input, app.config['UPLOAD_FOLDER'])
    return jsonify(response)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and file.filename.endswith('.pdf'):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return redirect(url_for('upload'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
