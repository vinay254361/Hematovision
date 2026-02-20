import tensorflow as tf
from tensorflow.keras import layers, models
import os

print("Creating a fresh MobileNetV2 model...")

# Create a fresh MobileNetV2-based model
base_model = tf.keras.applications.MobileNetV2(
    weights='imagenet', 
    include_top=False, 
    input_shape=(224, 224, 3)
)
base_model.trainable = False

# Create custom top layers
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dense(3, activation='softmax')  # 3 classes: RBC, WBC, Platelet
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Save the model
model_path = 'templates/blood_cell_classifier_mobilenetv2 (1).h5'
model.save(model_path)
print(f'Model saved successfully to {model_path}!')
