from BIC_CW.ANN.Network import Network
from BIC_CW.ANN.Layer import Layer

"""

ANN Builder adapted from pseudocode provided in canvas

Additional elements added to keep track of previous nodes (nodes in previous layers)

Minimum accepted layers is 3 (1 input, 1 hidden, 1 output)

"""


class ANNBuilder:
    def __init__(self):
        # initialize the Artificial Neural Network
        self.ann = Network()

    def build(self, nb_layers, list_nb_nodes, list_functions):
        """
        The ANN is builder is designed so the total number of layers in the network are sent
        From that total, the input layer, hidden layer(s), and output layer is recognized and
        created. This means the minimum number of layers to be made is 3, (ie. the minimum number
        of hidden layers is 1, since 1 input + 1 hidden + 1 output = 3)
        """
        # append the input layer
        nodes = list_nb_nodes[0]
        activation = list_functions[0]
        num_input = list_nb_nodes[0]
        input_layer = Layer(
            nodes=nodes, prev_nodes=0, activation=activation, num_input=num_input)
        self.ann.append(input_layer)

        # append the hidden layers
        for i in range(1, nb_layers-1):
            nodes = list_nb_nodes[i]
            prev_nodes = list_nb_nodes[i - 1]
            activation = list_functions[i]
            num_input = list_nb_nodes[i]
            layer = Layer(
                nodes=nodes, prev_nodes=prev_nodes, activation=activation, num_input=num_input)
            self.ann.append(layer)

        # append the output layer
        nodes = list_nb_nodes[-1]
        prev_nodes = list_nb_nodes[-2 if len(list_nb_nodes) > 1 else 0]
        activation = list_functions[-1]
        num_output = list_nb_nodes[-1]
        num_hidden = list_nb_nodes.size-2
        output_layer = Layer(
            nodes=nodes, prev_nodes=prev_nodes, activation=activation, num_output=num_output, num_hidden=num_hidden)
        self.ann.append(output_layer)

    def getANN(self):
        return self.ann
