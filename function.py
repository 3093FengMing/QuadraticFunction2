from numpy import ndarray
from sympy import *

from plot import *


def short(func):
    return func.replace(" ", "")[func.find("=") + 1:].replace("^", "**")


def calc_triangle(function1, function2, function3):
    if function1 == function2 or function1 == function3 or function2 == function3:
        print("两线重合")
        return

    x = Symbol('x')
    y = Symbol('y')
    f1 = sympify(short(function1) + "-y")
    f2 = sympify(short(function2) + "-y")
    f3 = sympify(short(function3) + "-y")
    solution1 = solve([f1, f2], [x, y])
    solution2 = solve([f1, f3], [x, y])
    solution3 = solve([f2, f3], [x, y])

    if len(solution1) != 2 or len(solution2) != 2 or len(solution3) != 2:
        print("两线重合或无交点")
        return
    dis1 = sqrt((solution1[x] - solution2[x]) ** 2 + (solution1[y] - solution2[y]) ** 2)
    dis2 = sqrt((solution1[x] - solution3[x]) ** 2 + (solution1[y] - solution3[y]) ** 2)
    dis3 = sqrt((solution2[x] - solution3[x]) ** 2 + (solution2[y] - solution3[y]) ** 2)

    p = (dis1 + dis2 + dis3) / 2
    area = sqrt(p * (p - dis1) * (p - dis2) * (p - dis3)).evalf()

    return area


class Function:
    def __init__(self, expression):
        self.expression = expression

    def calc_points(self, xlim=10):
        x = numpy.linspace(-xlim, xlim, 200 * xlim)
        y = eval(self.shorts())  # 效率↓ 省力↑
        if not isinstance(y, ndarray):
            value = y
            y = numpy.zeros(len(x))
            y.fill(value)
        return [x, y]

    def shorts(self):
        return self.expression.replace(" ", "")[self.expression.find("=") + 1:].replace("^", "**")
