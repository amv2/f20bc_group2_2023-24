import numpy as np

np.random.seed(300)


def calculate_accuracy(y_pred, y_true):
    binary_predictions = (y_pred > 0.5).astype(int)
    correct_predictions = np.sum(binary_predictions == y_true)
    total_samples = len(y_true)
    accuracy = correct_predictions / total_samples
    return accuracy


def calculate_loss(y_pred, y_true):
    # Assuming binary cross-entropy loss
    # Avoid log(0) which is undefined
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
    loss = -np.mean(y_true * np.log(y_pred) +
                    (1 - y_true) * np.log(1 - y_pred))
    return loss


def assess_fitness(particle, X, y, loss_function):
    # Decode particle's position to neural network weights and biases
    particle.update_nn_params(particle.position)

    # Forward pass through the neural network using the entire X dataset
    y_pred = particle.neural_network.forward(X)

    # Evaluate fitness using the loss function
    fitness = loss_function.evaluate(y_pred, y)

    # Calculate classification accuracy using all predictions
    accuracy = calculate_accuracy(y_pred, y)

    # Calculate loss
    loss = calculate_loss(y_pred, y)

    return fitness, accuracy, loss


def initialize_informants(particles, num_informants):
    for particle in particles:
        particle.informants = np.random.choice(
            particles, size=num_informants, replace=False).tolist()
