from engine.function import function
from engine.SolvingMethod import SolvingMethod
import numpy as np

class RungeKuttaMethod(SolvingMethod):
    def _computeY(self, x0, y0, X, N):
        h = (X - x0) / N
        self.y_array = np.empty(N + 1)
        self.y_array[0] = y0

        for i in range(1, N + 1):
            k1 = function.f(self.x_array[i-1], self.y_array[i-1])
            k2 = function.f(self.x_array[i - 1] + h / 2, self.y_array[i - 1] + h * k1 / 2)
            k3 = function.f(self.x_array[i - 1] + h / 2, self.y_array[i - 1] + h * k2 / 2)
            k4 = function.f(self.x_array[i - 1] + h, self.y_array[i - 1] + h * k3)

            self.y_array[i] = self.y_array[i-1] + 1 / 6 * h * (k1 + 2*k2 + 2*k3 + k4)

    def _computeLTE(self, x0, X, N):
        self.lte = np.empty(N + 1)
        h = (X - x0) / N
        for i in range(N + 1):
            k1 = function.f(self.x_array[i], self.y_array[i])
            k2 = function.f(self.x_array[i] + h / 2, self.y_array[i] + h * k1 / 2)
            k3 = function.f(self.x_array[i] + h / 2, self.y_array[i] + h * k2 / 2)
            k4 = function.f(self.x_array[i] + h, self.y_array[i] + h * k3)

            self.lte[i] = (function.y(self.x_array[i]+h) -
                           function.y(self.x_array[i]) -
                           1 / 6 * h * (k1 + 2*k2 + 2*k3 + k4))
