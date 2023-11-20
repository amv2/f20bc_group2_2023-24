import numpy as np


class Loss:
    def evaluate(self, x):
        pass

    def derivative(self, x):
        pass


class Mse(Loss):
    def evaluate(self, y, t):
        return np.mean((t - y) ** 2)

    def derivative(self, y, t):
        return 2 * (y - t) / len(t)


class BinaryCrossEntropy(Loss):
    def evaluate(self, y, t):
        y_pred = np.clip(y, 1e-7, 1 - 1e-7)
        term0 = (1 - t) * np.log(1 - y_pred + 1e-7)
        term1 = t * np.log(y_pred + 1e-7)
        return -np.mean(term0 + term1)

    def derivative(self, y, t):
        return t / y + (1 - t) / (1 - y)


class Hinge(Loss):
    def evaluate(self, y, t):
        hinge_loss = np.maximum(0, 1 - t * y)
        return np.mean(hinge_loss)

    def derivative(self, y, t):
        margin = 1 - t * y
        grad = -t * (margin > 0).astype(int)
        return grad / len(t)
