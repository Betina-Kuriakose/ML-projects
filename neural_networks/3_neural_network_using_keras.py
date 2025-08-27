#symbolic math whether it is a cat or a dog so it is a predictive system
#step1: computation(extracts the size of each card, length,color..)
#step2: poooling(removes unnecessary data)
#step3: hidden layer/NN
#sequential= computation and pool layer
#dense= hidden layer(we dont have to create any hidden layer like fp and bp, it provies its own)
#categorical= convert complex to binary
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
from keras.utils import to_categorical
import sys


# Load and preprocess the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Reshape and normalize the image data
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# One-hot encode the labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Build the neural network model
model = Sequential()
model.add(Dense(units=512, activation='relu', input_shape=(28 * 28,)))
model.add(Dense(units=10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model and store training history
history = model.fit(
    train_images.reshape((60000, 28 * 28,1)),
    train_labels,
    epochs=10,
    batch_size=128,
    validation_data=(test_images.reshape((10000, 28 * 28,1)), test_labels)
)
# Plot training history

plt.figure(figsize=(12, 4))

# Plot training & validation loss values
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
# Plot training & validation accuracy values
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
#show the plots
plt.tight_layout()
plt.show()
