import numpy as np
from BIC_CW.PSO.Particle import Particle
from BIC_CW.PSO.PSOmethods import initialize_informants, assess_fitness

"""
Particle Swarm Optimixation implementation derived from the pseudocode given in the slides
"""

# np.random.seed(300)


def pso_with_informants(neural_network, X, y, loss_function, swarmsize, alpha, beta, gamma, delta, jump_size, max_iter, num_informants):
    # create all the particles according to the given swarm size
    particles = [Particle(neural_network) for _ in range(swarmsize)]
    # initially set the global best to none
    global_best = None

    # initialize informants randomly
    initialize_informants(particles, num_informants)

    for _ in range(max_iter):
        # for each particle, evaluate their fitness
        for particle in particles:
            fitness = assess_fitness(particle, X, y, loss_function)
            # update global best if it is better than current best
            if global_best is None or fitness < assess_fitness(global_best, X, y, loss_function):
                global_best = particle

        # for each particle check their informants' performance
        for particle in particles:
            personal_best = particle.best_position
            informants_best = max(
                particle.informants, key=lambda x: assess_fitness(x, X, y, loss_function)).best_position
            global_best_position = global_best.position

            b = np.random.uniform(0.0, beta)
            c = np.random.uniform(0.0, gamma)
            d = np.random.uniform(0.0, delta)

            # formula for updating velocity
            new_velocity = alpha * particle.velocity + b * (personal_best - particle.position) + \
                c * (informants_best - particle.position) + d * \
                (global_best_position - particle.position)

            # update the particle's velocity and position
            particle.velocity = new_velocity
            particle.position += jump_size * new_velocity

    return global_best
