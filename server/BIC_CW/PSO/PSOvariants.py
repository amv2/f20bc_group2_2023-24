import numpy as np
from BIC_CW.PSO.Particle import Particle
from BIC_CW.PSO.PSOmethods import initialize_informants, assess_fitness

np.random.seed(300)


def pso_with_informants(neural_network, X, y, loss_function, swarmsize, alpha, beta, gamma, delta, jump_size, max_iter, num_informants):
    particles = [Particle(neural_network) for _ in range(swarmsize)]
    global_best = None

    initialize_informants(particles, num_informants)

    for _ in range(max_iter):
        for particle in particles:
            fitness = assess_fitness(particle, X, y, loss_function)
            if global_best is None or fitness < assess_fitness(global_best, X, y, loss_function):
                global_best = particle

        for particle in particles:
            personal_best = particle.best_position
            informants_best = max(
                particle.informants, key=lambda x: assess_fitness(x, X, y, loss_function)).best_position
            global_best_position = global_best.position

            b = np.random.uniform(0.0, beta)
            c = np.random.uniform(0.0, gamma)
            d = np.random.uniform(0.0, delta)

            new_velocity = alpha * particle.velocity + b * (personal_best - particle.position) + \
                c * (informants_best - particle.position) + d * \
                (global_best_position - particle.position)

            particle.velocity = new_velocity
            particle.position += jump_size * new_velocity

    return global_best


def pso_with_social_learning(neural_network, X, y, loss_function, swarmsize, alpha, beta, gamma, delta, jump_size, max_iter, num_informants):
    particles = [Particle(neural_network) for _ in range(swarmsize)]
    global_best = None

    for _ in range(max_iter):
        for particle in particles:
            fitness = assess_fitness(particle, X, y, loss_function)
            if global_best is None or fitness < assess_fitness(global_best, X, y, loss_function):
                global_best = particle

        # Assign informants to particles
        for i, particle in enumerate(particles):
            informants = []
            for j in range(max(i - num_informants // 2, 0), min(i + num_informants // 2, swarmsize)):
                if i != j:
                    informants.append(particles[j])
            particle.informants = informants

        for particle in particles:
            personal_best = particle.best_position
            informants_best = max(
                particle.informants, key=lambda x: assess_fitness(x, X, y, loss_function)).best_position
            global_best_position = global_best.position

            b = np.random.uniform(0.0, beta)
            c = np.random.uniform(0.0, gamma)
            d = np.random.uniform(0.0, delta)

            new_velocity = alpha * particle.velocity + b * (personal_best - particle.position) + \
                c * (informants_best - particle.position) + d * \
                (global_best_position - particle.position)

            particle.velocity = new_velocity
            particle.position += jump_size * new_velocity

    return global_best


def pso_with_constriction(neural_network, X, y, loss_function, swarmsize, alpha, beta, gamma, delta, jump_size, max_iter, num_informants):
    particles = [Particle(neural_network) for _ in range(swarmsize)]
    global_best = None

    phi = beta + gamma + delta
    discriminant = phi ** 2 - 4 * phi

    # Check if the discriminant is non-negative before computing square root
    if discriminant >= 0:
        constriction_factor = 2 / abs(2 - phi - np.sqrt(discriminant))
    else:
        # Handle the case where the discriminant is negative
        constriction_factor = 1  # Assign a default value or handle accordingly

    for _ in range(max_iter):
        for particle in particles:
            fitness = assess_fitness(particle, X, y, loss_function)
            if global_best is None or fitness < assess_fitness(global_best, X, y, loss_function):
                global_best = particle

        for i, particle in enumerate(particles):
            informants = []
            for j in range(max(i - num_informants // 2, 0), min(i + num_informants // 2, swarmsize)):
                if i != j:
                    informants.append(particles[j])
            particle.informants = informants

        for particle in particles:
            personal_best = particle.best_position
            informants_best = max(
                particle.informants, key=lambda x: assess_fitness(x, X, y, loss_function)).best_position
            global_best_position = global_best.position

            new_velocity = constriction_factor * (particle.velocity +
                                                  alpha * np.random.rand() * (personal_best - particle.position) +
                                                  beta * np.random.rand() * (informants_best - particle.position) +
                                                  gamma * np.random.rand() * (global_best_position - particle.position))

            particle.velocity = new_velocity
            particle.position += jump_size * new_velocity

    return global_best
