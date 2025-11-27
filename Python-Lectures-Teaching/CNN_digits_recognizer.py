import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build model (added dropout + extra layer for better learning)
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model
model.fit(x_train, y_train, epochs=3)

# Evaluate model
loss, acc = model.evaluate(x_test, y_test)
print("Test Accuracy:", acc)

# Predict a sample with extra details
def predict_sample(index=0):
    sample = x_test[index]
    plt.imshow(sample, cmap='gray')
    plt.title(f"Sample Image (Index: {index})")
    plt.show()

    pred = model.predict(sample.reshape(1, 28, 28))
    print("Predicted digit:", pred.argmax())

# Example prediction
predict_sample(0)
