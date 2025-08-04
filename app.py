import os
import openai
from flask import Flask, request, render_template, jsonify, send_from_directory
from PIL import Image
import numpy as np
import tensorflow as tf
import json

app = Flask(__name__)

# Load OpenAI API key from environment variable or directly add your key here
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load class labels
with open('class_indices.json', 'r') as f:
    class_indices = json.load(f)

# For now, we'll create a simple placeholder model
# In a real application, you would load your trained model here
def create_simple_model():
    """Create a simple placeholder model for demonstration"""
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(224, 224, 3)),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, activation='relu'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(len(class_indices), activation='softmax')
    ])
    return model

# Initialize model
try:
    # Try to load from TensorFlow Hub (commented out due to compatibility issues)
    # model = hub.load("https://www.kaggle.com/models/rishitdagli/plant-disease/TensorFlow2/plant-disease/1")
    model = create_simple_model()
    print("Model initialized successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    model = create_simple_model()

def predict_image(image):
    try:
        image = image.resize((224, 224))
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)

        image = tf.convert_to_tensor(image, dtype=tf.float32)
        
        # For the placeholder model, we'll return a random prediction
        # In a real application, you would use: predictions = model(image)
        predictions = np.random.random((1, len(class_indices)))
        predictions = predictions / np.sum(predictions)  # Normalize to probabilities

        predicted_class_idx = np.argmax(predictions, axis=-1)[0]
        predicted_label = class_indices[str(predicted_class_idx)]
        return predicted_label
    except Exception as e:
        print(f"Error in prediction: {e}")
        return "Error in prediction"

# ChatGPT route to handle text input
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message received"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use gpt-4 or gpt-3.5-turbo depending on your API plan
            messages=[
                {"role": "system", "content": "You are an expert in plant diseases and their treatments."},
                {"role": "user", "content": user_message},
            ]
        )
        gpt_response = response['choices'][0]['message']['content']
        return jsonify({"response": gpt_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        image = Image.open(file)
        prediction = predict_image(image)
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
