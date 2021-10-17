from engine.function import function
from engine.SolvingMethod import SolvingMethod
import numpy as np

class ImprovedEulerMethod(SolvingMethod):
    def _computeY(self, x0, y0, X, N):
        h = (X - x0) / N
        self.y_array = np.empty(N + 1)
        self.y_array[0] = y0

        for i in range(1, N + 1):
            predict = self.y_array[i-1] + h * function.f(self.x_array[i-1], self.y_array[i-1])
            self.y_array[i] = (self.y_array[i-1] + h / 2 *
                               (function.f(self.x_array[i-1], self.y_array[i-1]) +
                                function.f(self.x_array[i], predict)))

    def _computeLTE(self, x0, X, N):
        self.lte = np.empty(N + 1)
        h = (X - x0) / N
        for i in range(N + 1):
            self.lte[i] = (function.y(self.x_array[i] + h) - function.y(self.x_array[i]) -
                           h * 1/2*(function.f(self.x_array[i], self.y_array[i]) +
                                    function.f(self.x_array[i] + h,
                                               self.y_array[i] +
                                               h * function.f(self.x_array[i], self.y_array[i]))))
