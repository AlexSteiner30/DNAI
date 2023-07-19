from flask import Flask, render_template, request, jsonify
import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    dna_sequence = data['dna_sequence']

    analysis_result = predict.predict(dna_sequence)

    return jsonify({'result': analysis_result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')