import time

from function import *

if __name__ == '__main__':
    T1 = time.perf_counter_ns()
    qfplot = Plot(xlimit=10, ylimit=10, hidden=False)
    l1 = Function("y=2*x+9")
    l2 = Function("y=-2*x+4")
    l3 = Function("y=-4*x-12")
    qfplot.show_functions(l1, l2, l3)
    s = calc_triangle("y=2*x+9", "y=-2*x+4", "y=-4*x-12")
    print(s)
    #qe = uqe.uqe("2x^2-10x")
    #print(qe.solve())
    print(f"耗时：{(time.perf_counter_ns()-T1)/1000/1000}毫秒")
