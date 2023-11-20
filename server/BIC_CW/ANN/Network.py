class Network:
    def __init__(self):
        # Initialize the empty list of layers
        self.layers = []

    def append(self, layer):
        # Append a layer to the network
        self.layers.append(layer)

    def forward(self, data_in):
        out = data_in
        for layer in self.layers:
            out = layer.forward(out)
        return out

    def backpropagate(self, delta, rate):
        # Delta initially holds the derivative of the loss
        for layer in reversed(self.layers):
            delta = layer.backpropagate(delta, rate)
