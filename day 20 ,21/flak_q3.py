
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = data['features']
        
        if not isinstance(features, list) or len(features) != 2:
            raise ValueError
        if not all(isinstance(x, (int, float)) for x in features):
            raise ValueError
            
        prediction = model.predict([features])[0]
        return jsonify({'prediction': int(prediction)})
    
    except Exception as e:
        return jsonify({'error': 'Invalid input format'}), 400

if __name__ == '__main__':
    app.run(debug=True)