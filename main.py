import time

import plot
import uqe

if __name__ == '__main__':
    T1 = time.perf_counter_ns()
    qfplot = plot.qfplot(10, 10, False)
    qfplot.show("y=9")
    #qe = uqe.uqe("2x^2-10x")
    #print(qe.solve())
    print(f"耗时：{(time.perf_counter_ns()-T1)/1000/1000}毫秒")
