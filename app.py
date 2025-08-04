import os
import openai
from flask import Flask, request, render_template, jsonify, send_from_directory
from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import json

app = Flask(__name__)

# Load OpenAI API key from environment variable or directly add your key here
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the TensorFlow model
model = hub.load("https://www.kaggle.com/models/rishitdagli/plant-disease/TensorFlow2/plant-disease/1")

# Load class labels
with open('class_indices.json', 'r') as f:
    class_indices = json.load(f)

def predict_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    image = tf.convert_to_tensor(image, dtype=tf.float32)
    predictions = model(image)

    predicted_class_idx = np.argmax(predictions, axis=-1)[0]
    predicted_label = class_indices[str(predicted_class_idx)]
    return predicted_label

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

    image = Image.open(file)
    prediction = predict_image(image)

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
