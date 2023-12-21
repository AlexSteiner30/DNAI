from flask import Flask, render_template, request, jsonify, send_file
import predict
import os

app = Flask(__name__, static_folder="static/")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    dna_sequence = data['dna_sequence']

    analysis_result = predict.predict(dna_sequence)

    return jsonify({'result': analysis_result})

@app.route('/download')
def download():
    return send_file("C:\\Users\\Marco\\Documents\\Programmazione\\Python\\DNAI\\main.py", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')