from flask import Flask, request, render_template, redirect, url_for, jsonify, session
from chatbot import chatbot_response
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Ganti dengan kunci rahasia yang aman
UPLOAD_FOLDER = 'uploads/'
HISTORY_FOLDER = 'history/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['HISTORY_FOLDER'] = HISTORY_FOLDER

if not os.path.exists(HISTORY_FOLDER):
    os.makedirs(HISTORY_FOLDER)

def save_history(history, filename):
    with open(os.path.join(app.config['HISTORY_FOLDER'], filename), 'w') as f:
        json.dump(history, f)

def load_history(filename):
    with open(os.path.join(app.config['HISTORY_FOLDER'], filename), 'r') as f:
        return json.load(f)

def list_histories():
    return [f for f in os.listdir(app.config['HISTORY_FOLDER']) if f.endswith('.json')]

@app.route('/')
def index():
    histories = list_histories()
    return render_template('index.html', histories=histories)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('message')
    history_name = request.form.get('history_name')
    history = load_history(history_name) if history_name else []
    response = chatbot_response(user_input, app.config['UPLOAD_FOLDER'])
    history.append({"user": user_input, "bot": response})
    if history_name:
        save_history(history, history_name)
    else:
        new_history_name = f"history_{len(history)}.json"
        save_history(history, new_history_name)
    return jsonify(response)

@app.route('/history/<history_name>')
def load_history_page(history_name):
    history = load_history(history_name)
    return render_template('index.html', history=history, histories=list_histories(), history_name=history_name)

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
