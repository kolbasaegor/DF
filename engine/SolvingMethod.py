from engine.function import function
import numpy as np

class SolvingMethod:
    def __init__(self):
        self.func = function()

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
        self.lte = np.empty(N + 1)

    def _computeGTE(self, N):
        self.gte = np.empty(N + 1)

        for i in range(N + 1):
            self.gte[i] = self.func.y(self.x_array[i]) - self.y_array[i]

    def computeED(self, range_from, range_to, x0, y0, X):
        self.nki = [i for i in range(range_from, range_to+1)]

        self.maxGTE = np.empty(len(self.nki))

        for i in range(range_from, range_to+1):
            self._computeX(x0, X, i)
            self._computeY(x0, y0, X, i)
            self._computeGTE(i)
            self.maxGTE[i - range_from] = max(self.gte)
            

