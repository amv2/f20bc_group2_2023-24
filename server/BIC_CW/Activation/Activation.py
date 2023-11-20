import numpy as np


class Activation:
    def evaluate(self, x):
        pass

    def derivative(self, x):
        pass


class Relu(Activation):
    def evaluate(self, x):
        return np.maximum(0, x)

    def derivative(self, x):
        return np.where(x > 0, 1, 0)


class Sigmoid(Activation):
    def evaluate(self, x):
        return 1 / (1 + np.exp(-x))

    def derivative(self, x):
        f = 1 / (1 + np.exp(-x))
        return f * (1 - f)


class Tanh(Activation):
    def evaluate(self, x):
        return np.tanh(x)

    def derivative(self, x):
        f = np.tanh(x)
        return 1 - f**2

# Additional activation functions


class Swish(Activation):
    def evaluate(self, x):
        return x * (1 / (1 + np.exp(-x)))

    def derivative(self, x):
        swish_x = x * (1 / (1 + np.exp(-x)))
        return swish_x + (1 / (1 + np.exp(-x))) * (1 - swish_x)


class Softmax(Activation):
    def evaluate(self, x):
        exp_vals = np.exp(x - np.max(x, axis=-1, keepdims=True))
        return exp_vals / np.sum(exp_vals, axis=-1, keepdims=True)

    def derivative(self, x):
        # The derivative of Softmax is a bit complex and involves the Jacobian matrix
        # Generally, in neural networks, derivative of Softmax is computed implicitly
        pass


class GELU(Activation):
    def evaluate(self, x):
        return x * 0.5 * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))))

    def derivative(self, x):
        cdf = 0.5 * (1 + np.tanh(np.sqrt(2 / np.pi) *
                     (x + 0.044715 * np.power(x, 3))))
        return 0.5 * (1 + np.tanh((np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))) + (0.107032 * np.power(x, 3))))
