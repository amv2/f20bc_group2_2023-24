from BIC_CW.ANN.Network import Network
from BIC_CW.ANN.Layer import Layer


class ANNBuilder:
    def __init__(self):
        self.ann = Network()

    def build(self, nb_layers, list_nb_nodes, list_functions):
        nodes = list_nb_nodes[0]
        activation = list_functions[0]
        num_input = list_nb_nodes[0]
        input_layer = Layer(
            nodes=nodes, prev_nodes=0, activation=activation, num_input=num_input)
        self.ann.append(input_layer)

        for i in range(1, nb_layers-1):
            nodes = list_nb_nodes[i]
            prev_nodes = list_nb_nodes[i - 1]
            activation = list_functions[i]
            num_input = list_nb_nodes[i]
            layer = Layer(
                nodes=nodes, prev_nodes=prev_nodes, activation=activation, num_input=num_input)
            self.ann.append(layer)

        nodes = list_nb_nodes[-1]
        prev_nodes = list_nb_nodes[-2]
        activation = list_functions[-1]
        num_output = list_nb_nodes[-1]
        num_hidden = list_nb_nodes.size-2
        output_layer = Layer(
            nodes=nodes, prev_nodes=prev_nodes, activation=activation, num_output=num_output, num_hidden=num_hidden)
        self.ann.append(output_layer)

    def getANN(self):
        return self.ann
