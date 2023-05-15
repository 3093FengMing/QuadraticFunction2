import matplotlib.pyplot as plt
import numpy

from numpy import ndarray


class qfplot:

    def __init__(self, xlimit, ylimit, hidden):
        self.xlimit = xlimit
        self.ylimit = ylimit
        self.hidden = hidden

    def calc(self, f):
        x = numpy.linspace(-self.xlimit, self.xlimit, 200 * self.xlimit)
        y = eval(f)  # 效率↓ 省力↑
        if not isinstance(y, ndarray):
            value = y
            y = numpy.zeros(len(x))
            y.fill(value)
        return [x, y]

    def show(self, func):
        print(f"函数: {func}")

        func = func.replace(" ", "")[func.find("=") + 1:].replace("^", "**")
        items = self.calc(func)

        # plt.title(func)
        plt.figure(num=1, figsize=(self.xlimit, self.ylimit))

        plt.plot(items[0], items[1], color='red', linewidth=1, linestyle='-')
        plt.xlim(-self.xlimit, self.xlimit)
        plt.ylim(-self.ylimit, self.ylimit)
        plt.xlabel('x', loc="right")
        plt.ylabel('y', loc="top")

        plt.xticks(numpy.arange(-self.xlimit, self.xlimit + 1, 1))
        plt.yticks(numpy.arange(-self.ylimit, self.ylimit + 1, 1))

        ax = plt.gca()
        if self.hidden:
            ax.axes.xaxis.set_ticklabels([])
            ax.axes.yaxis.set_ticklabels([])

        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data', 0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data', 0))

        plt.grid(True)
        plt.show()
