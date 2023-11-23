"""

Network class adapted from pseudocode provided in canvas

"""


class Network:
    def __init__(self):
        # Initialize the empty list of layers
        self.layers = []

    def append(self, layer):
        # Append a layer to the network
        self.layers.append(layer)

    def forward(self, data_in):
        # forward propagation using the forward method in the Layer class
        out = data_in
        for layer in self.layers:
            out = layer.forward(out)
        return out

    def backpropagate(self, delta, rate):
        # optional back propagation
        for layer in reversed(self.layers):
            delta = layer.backpropagate(delta, rate)
