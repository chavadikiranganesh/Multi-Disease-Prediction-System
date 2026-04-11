import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import numpy as np

# Create a simple CNN model for skin disease detection as a temporary replacement
def create_simple_skin_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(9, activation='softmax')  # 9 skin disease classes
    ])
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Create and save the model
print("Creating simple skin model...")
skin_model = create_simple_skin_model()

# Save the model
skin_model.save('models/skin_model_simple.h5')
print("Simple skin model saved as 'models/skin_model_simple.h5'")

# Also update the app.py to use this model
print("\nTo use this model:")
print("1. Replace 'skin_model.h5' with 'skin_model_simple.h5' in app.py")
print("2. Or rename 'skin_model_simple.h5' to 'skin_model.h5'")
