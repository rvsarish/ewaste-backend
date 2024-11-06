from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import cv2

app = Flask(__name__)

# Load the pre-trained modelI
model = load_model('ewaste_classification_model.h5')

# Define the categories (ensure these match your training labels)
categories = ['keyboard', 'laptop', 'mobile', 'monitor', 'mouse', 'mixed']

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (150, 150))  # Resize to match model input
    img = img.astype('float32') / 255.0  # Normalize
    img = np.expand_dims(img, axis=0)  # Add batch dimension

    # Make prediction
    prediction = model.predict(img)
    predicted_category = categories[np.argmax(prediction)]
    
    return jsonify({'prediction': predicted_category})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

