import numpy as np

"""

Methods used by Particle Swarm Optimization

Informants are randomly allocated

Accuracy computed by comparing predicted labels with true labels

"""

# np.random.seed(300)


def calculate_accuracy(y_pred, y_true):
    binary_predictions = (y_pred > 0.5).astype(int)
    correct_predictions = np.sum(binary_predictions == y_true)
    total_samples = len(y_true)
    accuracy = correct_predictions / total_samples
    return accuracy


def assess_fitness(particle, X, y, loss_function):
    # Decode particle's position to neural network weights and biases
    particle.update_nn_params(particle.position)

    # Forward pass through the neural network using the entire X dataset
    y_pred = particle.neural_network.forward(X)

    # find fitness and loss
    fitness = loss_function.evaluate(y_pred, y)
    loss = 1 / (1 + fitness)

    # Calculate classification accuracy using all predictions
    accuracy = calculate_accuracy(y_pred, y)

    return accuracy, fitness, loss


def initialize_informants(particles, num_informants):
    # initialize the informants for each particle randomly
    for particle in particles:
        # select according to the number of informants
        particle.informants = np.random.choice(
            particles, size=num_informants, replace=False).tolist()
