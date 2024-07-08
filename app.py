from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

@app.route('/')
def home():
    return render_template('password.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    password = generate_password(length)
    return jsonify(password=password)

if __name__ == '__main__':
    app.run(debug=True)
