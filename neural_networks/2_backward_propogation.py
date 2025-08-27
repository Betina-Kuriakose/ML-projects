import numpy as np
import matplotlib.pyplot as plt
input_size = 2
hidden_size = 3
output_size = 1
learning_rate = 0.01#(can be 0 to 1)slower the learning rate better the accuracy
epochs = 10000 #number of times the model will be trained from input to hidden to output layer

#initialize 
#np.random.seed(42) # for reproducibility
weights_input_hidden = np.random.rand(input_size, hidden_size)
weights_hidden_output = np.random.rand(hidden_size, output_size)
bias_hidden = np.zeros((1,hidden_size))
bias_output = np.zeros((1, output_size))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#mean squared error loss
def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

#train data
x= np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) # XOR input
y= np.array([[0], [1], [1], [0]])  # XOR output

#model training
loses = []
for epoch in range(epochs):
    # Forward pass
    hidden_layer_input = np.dot(x, weights_input_hidden) + bias_hidden
    hidden_output= sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_output, weights_hidden_output) + bias_output
    predicted_output=sigmoid(output_layer_input)
    #calculate loss
    loss= mse_loss(y, predicted_output)
    loses.append(loss)
    # Backward pass
    output_error = y- predicted_output
    #  
    output_delta = output_error *sigmoid( predicted_output) * (1 -sigmoid( predicted_output))#output layer error to hidden layer

    hidden_error = output_delta.dot(weights_hidden_output.T)# calculate error for hidden layer to output layer
    hidden_delta = hidden_error * sigmoid(hidden_output) * (1 - sigmoid(hidden_output))

    #update weights and biases
    weights_hidden_output += hidden_output.T.dot(output_delta) * learning_rate
    weights_input_hidden += x.T.dot(hidden_delta) * learning_rate
    bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    # plotting the loss
    # if epoch % 1000 == 0:
    #     print(f'Epoch {epoch}, Loss: {loss}')
    # Plotting the loss
plt.plot(range(epochs), loses)
plt.xlabel('Epochs')
plt.ylabel('mean square error Loss')
plt.title('Training Loss over epochs')
plt.show()

test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predicted_output = sigmoid(np.dot(sigmoid(np.dot(test_data, weights_input_hidden) + bias_hidden), weights_hidden_output) + bias_output)
print("Predicted output after training:")
print(predicted_output)