import matplotlib.pyplot as plt
import numpy


class Plot:

    def __init__(self, hidden, xlimit=10, ylimit=10):
        self.xlimit = xlimit
        self.ylimit = ylimit
        self.hidden = hidden

    def init_plot(self):
        plt.figure(num=1, figsize=(self.xlimit, self.ylimit))

        # plt.title(func)

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

    def show_points(self, *points):
        self.init_plot()
        for point in points:
            plt.plot(point[0], point[1], color='red', linewidth=1, linestyle='-')
        plt.show()

    def show_functions(self, *functions):
        self.init_plot()
        for f in functions:
            points = f.calc_points()
            plt.plot(points[0], points[1], color='red', linewidth=1, linestyle='-')
        plt.show()
