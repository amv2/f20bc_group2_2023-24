import numpy as np

"""

Code adapted from given pseudocode from canvas

Additonal variables added to keep track of input, hidden, and output layer(s)

Backpropagation added

"""

# set a random seed for randomly generated values
# np.random.seed(300)


class Layer:
    def __init__(self, nodes, prev_nodes, activation, **kwargs):
        # set the layer variables
        self.nodes = nodes
        self.activation = activation
        self.X_in = None
        self.W = np.random.randn(
            prev_nodes, nodes) if prev_nodes > 0 else np.random.randn(nodes, nodes)
        self.B = np.random.randn(nodes)

        # set the input, hidden, and output layers optionally
        # ie. if the current Layer object is an input layer
        # only the input layer will be set to a value beside 0
        self.num_input = 0
        self.num_output = 0
        self.num_hidden = 0

        if 'num_input' in kwargs:
            self.num_input = kwargs['num_input']

        if 'num_output' in kwargs:
            self.num_output = kwargs['num_output']
            self.num_hidden = kwargs['num_hidden']

    def forward(self, _input):
        # set the X_in
        self.X_in = _input
        # compute the dot product of the data and weights then add the bias
        z = np.dot(_input, self.W) + self.B
        # evaluate with the activation function
        out = self.activation.evaluate(z)
        out = z
        # Ensure output shape matches the shape of y
        if out.ndim == 2 and out.shape[1] == 1:
            out = out.flatten()  # Convert to a 1D array if it's a column vector

        return out

    def backpropagate(self, delta, rate):
        # optional backpropagation
        dz = self.activation.derivative(
            np.dot(self.X_in, self.W) + self.B) * delta
        dw = np.outer(self.X_in, dz)
        db = dz
        new_delta = np.dot(dz, self.W.T)

        # update the weights and biases
        self.W -= rate * dw
        self.B -= rate * db

        return new_delta
