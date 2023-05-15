import numpy


class uqe:
    a = 0
    b = 0
    c = 0
    equation = ""  # 2x^2+3x+4

    def __init__(self, e):
        e = e.replace("-", "+-")
        self.equation = e
        items = e.replace(" ", "").split("+")
        if len(items) == 1:
            items.append("0x")
            items.append("0")
        if len(items) == 2:
            items.append("0")
        self.a = float(items[0][:items[0].rfind("x^2")])
        self.b = float(items[1][:items[1].rfind("x")])
        self.c = float(items[2])

    def solve(self):
        return f"{-(self.b/2*self.a)}±√{numpy.float_power(self.b/2*self.a, 2)-self.c/self.a}"
