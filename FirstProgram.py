import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Training dataset: 4 samples, 3 features each
inputs = np.array([[0,0,1],
                   [1,1,1],
                   [1,0,1],
                   [0,1,1]])

# Output dataset: target values
outputs = np.array([[0],[1],[1],[0]])

np.random.seed(1)
weights = 2 * np.random.random((3, 1)) - 1

# Training loop
for _ in range(10000):
    input_layer = inputs
    predictions = sigmoid(np.dot(input_layer, weights))
    error = outputs - predictions
    adjustments = error * sigmoid_derivative(predictions)
    weights += np.dot(input_layer.T, adjustments)

print("Predictions after training:")
print(predictions)
