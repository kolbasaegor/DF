import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from engine.EulerMethod import EulerMethod
from engine.ImprovedEulerMethod import ImprovedEulerMethod
from engine.RungeKuttaMethod import RungeKuttaMethod
from engine.function import function

class MplCanvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        self.ax.set(xlabel='x', ylabel='y', title="y' = y / x + x * cos(x)")
        self.ax.grid()
        super().__init__(fig)
        self.setParent(parent)

        self.parent = parent
        self.e = EulerMethod()
        self.ie = ImprovedEulerMethod()
        self.rk = RungeKuttaMethod()


    def plot(self, eulerMethodVisible, improvedEulerMethod,
             rungeKuttaVisible, x0, y0, X, N):


        plt.cla()
        self.ax.set(xlabel='x', ylabel='y', title="y' = y / x + x * cos(x)")
        self.ax.grid()
        self.e.compute(x0, y0, X, N)
        h = (X - x0) / max(100, N)
        x = np.empty(max(100, N) + 1)
        x[0] = x0
        for i in range(1, max(100, N) + 1):
            x[i] = x[i-1] + h

        self.ax.plot(x, [function.y(i) for i in x], label="Exact Solution")

        if eulerMethodVisible:
            self.e.compute(x0, y0, X, N)
            self.ax.plot(self.e.x_array, self.e.y_array, label="Euler Method")

        if improvedEulerMethod:
            self.ie.compute(x0, y0, X, N)
            self.ax.plot(self.ie.x_array, self.ie.y_array, label="Improved Euler")

        if rungeKuttaVisible:
            self.rk.compute(x0, y0, X, N)
            self.ax.plot(self.rk.x_array, self.rk.y_array, label="Runge-Kutta")

        plt.legend()
        self.draw()



