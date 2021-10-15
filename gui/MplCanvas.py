import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from engine.EulerMethod import EulerMethod
from engine.ImprovedEulerMethod import ImprovedEulerMethod
from engine.RungeKuttaMethod import RungeKuttaMethod
from engine.function import function

class MplCanvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        self.ax.set(xlabel='x', ylabel='y', title="Approximation")
        self.ax.grid()
        super().__init__(self.fig)
        self.setParent(parent)

        self.e = EulerMethod()
        self.ie = ImprovedEulerMethod()
        self.rk = RungeKuttaMethod()


    def plot(self, eulerMethodVisible, improvedEulerMethod,
             rungeKuttaVisible, x0, y0, X, N):


        plt.cla()
        self.ax.set(xlabel='x', ylabel='y', title="Approximation")
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

    def plotLTE(self, eulerMethodVisible, improvedEulerMethod,
             rungeKuttaVisible, x0, y0, X, N):

        plt.cla()
        self.ax.set(xlabel='x', ylabel='lte', title="Local Truncation Errors")
        self.ax.grid()


        if eulerMethodVisible:
            self.e.compute(x0, y0, X, N)
            self.ax.plot(self.e.x_array, self.e.lte, label="Euler Method LTE")

        if improvedEulerMethod:
            self.ie.compute(x0, y0, X, N)
            self.ax.plot(self.ie.x_array, self.ie.lte, label="Improved Euler LTE")

        if rungeKuttaVisible:
            self.rk.compute(x0, y0, X, N)
            self.ax.plot(self.rk.x_array, self.rk.lte, label="Runge-Kutta LTE")

        plt.legend()
        self.draw()

    def plotGTE(self, eulerMethodVisible, improvedEulerMethod,
             rungeKuttaVisible, x0, y0, X, N):

        plt.cla()
        self.ax.set(xlabel='x', ylabel='gte', title="Global Truncation Errors")
        self.ax.grid()


        if eulerMethodVisible:
            self.e.compute(x0, y0, X, N)
            self.ax.plot(self.e.x_array, self.e.gte, label="Euler Method GTE")

        if improvedEulerMethod:
            self.ie.compute(x0, y0, X, N)
            self.ax.plot(self.ie.x_array, self.ie.gte, label="Improved Euler GTE")

        if rungeKuttaVisible:
            self.rk.compute(x0, y0, X, N)
            self.ax.plot(self.rk.x_array, self.rk.gte, label="Runge-Kutta GTE")

        plt.legend()
        self.draw()




