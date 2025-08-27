import numpy as np
#activation functions
def sigmoid(x):
    return 1/(1 +np.exp(-x))

def forward_propagation(X,weights,baias):
    #inpur layer to hidden layer
    z1=np.dot(X,weights['W1'])+ baias['b1']
    a1=sigmoid(z1)
    #hidden layer to output layer
    z2=np.dot(a1,weights['W2'])+ baias['b2']
    a2=sigmoid(z2)
    return a2  #output of neural network
#data define
input_size=3
hidden_size=4
output_size=1

np.random.seed(42)  
weights={
    'W1': np.random.rand(input_size, hidden_size),
    'W2': np.random.rand(hidden_size, output_size)
}
baias={
    'b1': np.zeros((1, hidden_size)),
    'b2': np.zeros((hidden_size, output_size))
}

#input data
X = np.array([0.5,0.6,0.1])
output= forward_propagation(X, weights, baias)
print("Input data:", X)
print("output ",output)