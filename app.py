from flask import Flask, render_template, request, jsonify
from model import predict_emotion   # function from model.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.json['message']
    result = predict_emotion(user_input)
    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(debug=True)