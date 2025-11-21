import tensorflow as tf
import numpy as np
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array

from google.colab import files   

# step1 loading the dataset
data, info = tfds.load("rock_paper_scissors", with_info=True, as_supervised=True)
train, test = data["train"], data["test"]  

#step 2 
IMG = 25
def preprocessing(img, label1):
    img = tf.image.resize(img, (IMG, IMG)) / 255.0   
    return img, label1

train = train.map(preprocessing).batch(32)
test = test.map(preprocessing).batch(32)

classes = ["rock", "paper", "scissors"]

#  model training  layers
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(IMG, IMG, 3)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

# train 
model.fit(train, epochs=5, validation_data=test)

#saving and loading data
model.save("rps.h5")
model = tf.keras.models.load_model("rps.h5")

# prediction
def prediction(path):
    img = load_img(path, target_size=(IMG, IMG))
    arr = np.expand_dims(img_to_array(img) / 255.0, 0)
    pred = model.predict(arr)
    cls = classes[np.argmax(pred)]
    plt.imshow(load_img(path)); plt.axis("off")
    plt.title(f"{cls} — {np.max(pred)*100:.1f}%")
    plt.show()

# test
print("upload rock/paper/scissor image")
file_uploaded = files.upload()

for f in file_uploaded.keys():      
    prediction(f)
