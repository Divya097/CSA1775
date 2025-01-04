import math
import random

# Activation functions
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize weights and biases randomly
def initialize_matrix(rows, cols):
    return [[random.uniform(-1, 1) for _ in range(cols)] for _ in range(rows)]

def initialize_vector(size):
    return [random.uniform(-1, 1) for _ in range(size)]

# Feedforward Neural Network
class FeedforwardNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.weights_input_hidden = initialize_matrix(input_size, hidden_size)
        self.bias_hidden = initialize_vector(hidden_size)
        self.weights_hidden_output = initialize_matrix(hidden_size, output_size)
        self.bias_output = initialize_vector(output_size)

    def dot_product(self, vector, weights, bias):
        result = []
        for col in range(len(weights[0])):
            weighted_sum = sum(vector[row] * weights[row][col] for row in range(len(vector)))
            result.append(sigmoid(weighted_sum + bias[col]))
        return result

    def forward(self, inputs):
        # Input to hidden layer
        self.hidden_output = self.dot_product(inputs, self.weights_input_hidden, self.bias_hidden)

        # Hidden to output layer
        self.final_output = self.dot_product(self.hidden_output, self.weights_hidden_output, self.bias_output)

        return self.final_output

    def backward(self, inputs, expected_output, learning_rate):
        # Calculate output layer error and gradient
        output_errors = [expected_output[i] - self.final_output[i] for i in range(len(expected_output))]
        output_gradients = [output_errors[i] * sigmoid_derivative(self.final_output[i]) for i in range(len(output_errors))]

        # Update hidden-to-output weights and biases
        for i in range(self.hidden_size):
            for j in range(self.output_size):
                self.weights_hidden_output[i][j] += learning_rate * output_gradients[j] * self.hidden_output[i]
        for j in range(self.output_size):
            self.bias_output[j] += learning_rate * output_gradients[j]

        # Calculate hidden layer error and gradient
        hidden_errors = [
            sum(output_gradients[j] * self.weights_hidden_output[i][j] for j in range(self.output_size))
            for i in range(self.hidden_size)
        ]
        hidden_gradients = [hidden_errors[i] * sigmoid_derivative(self.hidden_output[i]) for i in range(self.hidden_size)]

        # Update input-to-hidden weights and biases
        for i in range(self.input_size):
            for j in range(self.hidden_size):
                self.weights_input_hidden[i][j] += learning_rate * hidden_gradients[j] * inputs[i]
        for j in range(self.hidden_size):
            self.bias_hidden[j] += learning_rate * hidden_gradients[j]

    def train(self, inputs, expected_outputs, epochs, learning_rate):
        for epoch in range(epochs):
            for input_vector, expected_output in zip(inputs, expected_outputs):
                self.forward(input_vector)
                self.backward(input_vector, expected_output, learning_rate)

# Example: XOR problem
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
outputs = [[0], [1], [1], [0]]

# Initialize and train the network
nn = FeedforwardNeuralNetwork(input_size=2, hidden_size=4, output_size=1)
nn.train(inputs, outputs, epochs=10000, learning_rate=0.1)

# Test the network
for input_vector in inputs:
    output = nn.forward(input_vector)
    print(f"Input: {input_vector}, Predicted Output: {output}")
