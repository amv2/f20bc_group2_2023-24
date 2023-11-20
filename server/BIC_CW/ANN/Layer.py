import numpy as np

np.random.seed(300)


class Layer:
    def __init__(self, nodes, prev_nodes, activation, **kwargs):
        self.nodes = nodes
        self.activation = activation
        self.X_in = None
        self.W = np.random.randn(
            prev_nodes, nodes) if prev_nodes > 0 else np.random.randn(nodes, nodes)
        self.B = np.random.randn(nodes)

        # modification
        self.num_input = 0
        self.num_output = 0
        self.num_hidden = 0

        if 'num_input' in kwargs:
            self.num_input = kwargs['num_input']

        if 'num_output' in kwargs:
            self.num_output = kwargs['num_output']
            self.num_hidden = kwargs['num_hidden']

        # Initialize weights and biases
        self.weights_input_hidden = np.random.randn(
            self.num_hidden, self.num_input)
        self.bias_hidden = np.random.randn(self.num_hidden)
        self.weights_output_hidden = np.random.randn(
            self.num_hidden, self.num_output)
        self.bias_output = np.random.randn(self.num_output)

    def forward(self, _input):
        self.X_in = _input
        z = np.dot(_input, self.W) + self.B
        # out = self.activation.evaluate(z)
        out = z

        # Ensure output shape matches the shape of y
        if out.ndim == 2 and out.shape[1] == 1:
            out = out.flatten()  # Convert to a 1D array if it's a column vector

        return out

    def backpropagate(self, delta, rate):
        dz = self.activation.derivative(
            np.dot(self.X_in, self.W) + self.B) * delta
        dw = np.outer(self.X_in, dz)
        db = dz
        new_delta = np.dot(dz, self.W.T)

        self.W -= rate * dw
        self.B -= rate * db

        return new_delta
