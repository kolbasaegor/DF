from engine.SolvingMethod import SolvingMethod
import numpy as np

class EulerMethod(SolvingMethod):
    def __init__(self):
        super().__init__()

    def _computeY(self, x0, y0, X, N):
        h = (X - x0) / N
        self.y_array = np.empty(N + 1)
        self.y_array[0] = y0

        for i in range(1, N + 1):
            self.y_array[i] = (self.y_array[i-1] +
                               h * self.func.f(self.x_array[i-1], self.y_array[i-1]))

    def _computeLTE(self, x0, X, N):
        self.lte = np.empty(N + 1)
        h = (X - x0) / N
        for i in range(N + 1):
            self.lte[i] = (self.func.y(self.x_array[i] + h) - self.func.y(self.x_array[i]) -
                           h * self.func.f(self.x_array[i], self.y_array[i]))
