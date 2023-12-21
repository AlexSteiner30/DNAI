from flask import Flask, render_template, request, jsonify, send_file
import predict
import os

app = Flask(__name__, static_folder="static/")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    count = 1

    data = request.get_json()
    dna_sequence = data['dna_sequence']

    analysis_result = predict.predict(dna_sequence, count)
    count = count + 1

    return jsonify({'result': analysis_result})

@app.route('/download')
def download():
    return send_file(f"static/analysis/analysis_{str(1)}.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')