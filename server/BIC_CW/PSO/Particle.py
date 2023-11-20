import numpy as np

np.random.seed(300)


class Particle:
    def __init__(self, neural_network):
        self.neural_network = neural_network
        self.position = self.flatten_params(neural_network)
        self.velocity = np.random.rand(len(self.position))
        self.best_position = self.position.copy()
        self.informants = []

    def flatten_params(self, neural_network):
        params = []
        for layer in neural_network.layers:
            params.extend(layer.W.flatten())
            params.extend(layer.B)
        return np.array(params)

    def update_nn_params(self, params):
        index = 0
        for i in range(len(self.neural_network.layers)):
            layer = self.neural_network.layers[i]
            size_W = layer.W.size
            size_B = layer.B.size
            layer.W = params[index:index+size_W].reshape(layer.W.shape)
            index += size_W
            layer.B = params[index:index+size_B]
            index += size_B
