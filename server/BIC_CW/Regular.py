"""

Method to take in all hyper parameters for ANN and PSO

And then run PSO to fit the ANN to the given data set

"""

"""
IMPORTS
"""


# np.random.seed(300)

import numpy as np
import pandas as pd
from BIC_CW.ANN.ANNBuilder import ANNBuilder
from BIC_CW.PSO.PSOmethods import assess_fitness
from BIC_CW.PSO.PSOvariants import pso_with_informants
from BIC_CW.Activation.Activation import Sigmoid, Relu, Tanh, LeakyReLU, Swish, Softmax, GELU
from BIC_CW.Loss.Loss import Mse, BinaryCrossEntropy, Hinge
import time
input_features = 4


# Access the directory path
data_path = "BIC_CW/zdata/data_banknote_authentication.csv"


def regular_run(nb_layers,
                nb_nodes,
                list_func,
                loss_func,
                swarmsize,
                alpha,
                beta,
                gamma,
                delta,
                jump_size,
                max_iter,
                num_informants):
    start_time = time.time()

    data = pd.read_csv(data_path)
    X = data.drop(data.columns[-1], axis=1).values
    # y = data.iloc[:, -1].values
    y = data.iloc[:, -1].values.flatten()

    """
    ANN
    """

    builder = ANNBuilder()

    nb_layers = nb_layers
    list_nb_nodes = np.full(nb_layers, nb_nodes)  # higher is better
    ###

    list_nb_nodes[0] = input_features
    list_nb_nodes[-1] = 1
    print(list_nb_nodes)

    activation_function = Relu()  # default activation function

    # change due to the index in Regular.js
    list_func = list_func - 1
    # encode the activation functions
    if list_func == 1:
        activation_function = Relu()
    elif list_func == 2:
        activation_function = Sigmoid()
    elif list_func == 3:
        activation_function = Tanh()
    elif list_func == 4:
        activation_function = LeakyReLU()
    elif list_func == 5:
        activation_function = Swish()
    elif list_func == 6:
        activation_function = Softmax()
    elif list_func == 7:
        activation_function = GELU()

    list_functions = np.full(nb_layers, activation_function)

    builder.build(nb_layers=nb_layers,
                  list_nb_nodes=list_nb_nodes,
                  list_functions=list_functions)

    nn = builder.getANN()

    """
    PSO
    """

    loss_function = BinaryCrossEntropy()  # default loss function

    # change due to the index in Regular.js
    loss_func = loss_func - 1
    # encode the loss function
    if loss_func == 1:
        loss_function = Mse()
    elif loss_func == 2:
        loss_function = BinaryCrossEntropy()
    if loss_func == 3:
        loss_function = Hinge()

    # PSO parameters
    swarmsize = swarmsize
    alpha, beta, gamma, delta = alpha, beta, gamma, delta
    jump_size = jump_size
    max_iter = max_iter
    num_informants = num_informants

    """
    SOLUTION
    """

    best_solution = pso_with_informants(
        nn, X, y, loss_function, swarmsize, alpha, beta, gamma, delta, jump_size, max_iter, num_informants)

    accuracy, fitness, loss = assess_fitness(
        best_solution, X, y, loss_function)

    print("Best Solution:", best_solution.position)
    print("Accuracy:", accuracy)
    print("Fitness:", fitness)
    print("Loss:", loss)

    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")

    return accuracy, fitness, loss, elapsed_time
