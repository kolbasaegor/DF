from engine.function import function
from engine.SolvingMethod import SolvingMethod
import numpy as np

class EulerMethod(SolvingMethod):
    def _computeY(self, x0, y0, X, N):
        h = (X - x0) / N
        self.y_array = np.empty(N + 1)
        self.y_array[0] = y0

        for i in range(1, N + 1):
            self.y_array[i] = (self.y_array[i-1] +
                               h * function.f(self.x_array[i-1] , self.y_array[i-1]))


