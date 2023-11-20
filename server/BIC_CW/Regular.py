"""
IMPORTS
"""

import numpy as np
import pandas as pd


from BIC_CW.ANN.ANNBuilder import ANNBuilder
from BIC_CW.PSO.PSOmethods import assess_fitness
from BIC_CW.PSO.PSOvariants import pso_with_informants, pso_with_social_learning, pso_with_constriction

from BIC_CW.Activation.Activation import Sigmoid, Relu, Tanh, Swish, Softmax, GELU
from BIC_CW.Loss.Loss import Mse, BinaryCrossEntropy, Hinge

from dotenv import dotenv_values
import time

np.random.seed(300)


def regular_run(data_path,
                nb_layers,
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
                num_informants,
                pso_type):
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

    list_nb_nodes[0] = 4
    list_nb_nodes[-1] = 1
    print(list_nb_nodes)
    list_functions = np.full(nb_layers, Relu())

    builder.build(nb_layers=nb_layers,
                  list_nb_nodes=list_nb_nodes,
                  list_functions=list_functions)

    nn = builder.getANN()

    """
    PSO
    """

    loss_function = BinaryCrossEntropy()

    # PSO parameters
    swarmsize = swarmsize
    alpha, beta, gamma, delta = alpha, beta, gamma, delta
    jump_size = jump_size
    max_iter = max_iter
    num_informants = num_informants

    """
    SOLUTION
    """

    best_solution = pso_with_constriction(
        nn, X, y, loss_function, swarmsize, alpha, beta, gamma, delta, jump_size, max_iter, num_informants)

    fitness, accuracy, loss = assess_fitness(
        best_solution, X, y, loss_function)

    print("Best Solution:", best_solution.position)
    print("Fitness:", fitness)
    print("Accuracy:", accuracy)
    print("Loss:", loss)

    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")

    print("Seed 300")

    return accuracy, fitness, loss


# Seed 300: 96%
