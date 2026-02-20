import tensorflow as tf
from flask import Flask, render_template, request
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Load the pre-trained model
try:
    model = tf.keras.models.load_model('templates/blood_cell_classifier_mobilenetv2 (1).h5')
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Class names (adjust based on your training classes)
CLASS_NAMES = ['RBC', 'WBC', 'Platelet']  # Adjust these based on your actual classes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return 'Error: Model not loaded', 500
    
    if 'file' not in request.files:
        return 'Error: No file uploaded', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'Error: No file selected', 400
    
    if file:
        # Ensure images directory exists
        images_dir = os.path.join('static', 'images')
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)
        
        # Save the file with a unique name
        filename = secure_filename(file.filename)
        filepath = os.path.join(images_dir, filename)
        file.save(filepath)
        
        try:
            # Load and preprocess the image
            img = load_img(filepath, target_size=(224, 224))
            img_array = img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            
            # Make prediction
            predictions = model.predict(img_array, verbose=0)
            predicted_class = np.argmax(predictions[0])
            confidence = float(predictions[0][predicted_class])
            
            result = {
                'prediction': CLASS_NAMES[predicted_class],
                'confidence': f'{confidence * 100:.2f}%',
                'image_file': filename
            }
            
            return render_template('result.html', **result)
        
        except Exception as e:
            return f'Error during prediction: {str(e)}', 500
    
    return 'Error: Upload failed', 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)