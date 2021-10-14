import math

class function:

    @staticmethod
    def f(x, y):
        return y / x + x * math.cos(x)

    @staticmethod
    def y(x):
        return x * math.sin(x) + x / math.pi
