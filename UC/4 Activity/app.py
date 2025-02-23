from flask import Flask, request, jsonify
import joblib
import numpy as np

file_path="knnModel.pkl"
model = joblib.load(file_path)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        x = data['x']
        y = data['y']
        z = data['z']
        
        ip = np.array([x, y, z], dtype=np.float64).reshape(1, -1)  

        prediction = model.predict(ip)
        print(f"Prediction: {prediction}")

        # Return the prediction as JSON
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        print(f"Error: {str(e)}") 
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
