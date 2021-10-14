from engine.function import function
import numpy as np

class SolvingMethod:
    def compute(self, x0, y0, X, N):
        self._computeX(x0, X, N)
        self._computeY(x0, y0, X, N)
        self._computeLTE(x0, X, N)
        self._computeGTE(N)

    def _computeX(self, x0, X, N):
        h = (X - x0) / N
        self.x_array = np.empty(N + 1)
        self.x_array[0] = x0

        for i in range(1, N + 1):
            self.x_array[i] = self.x_array[i - 1] + h

    def _computeY(self, x0, y0, X, N):
        self.y_array = np.empty(N + 1)


    def _computeLTE(self, x0, X, N):
        h = (X - x0) / N
        self.lte = np.empty(N + 1)
        self.lte[0] = 0

        for i in range(1, N + 1):
            self.lte[i] = (function.y(self.x_array[i]) - function.y(self.x_array[i - 1]) -
                           h * function.f(self.x_array[i - 1], function.y(self.x_array[i - 1])))

    def _computeGTE(self, N):
        self.gte = np.empty(N + 1)

        for i in range(N + 1):
            self.gte[i] = function.y(self.x_array[i]) - self.y_array[i]
