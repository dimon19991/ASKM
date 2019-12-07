from math import exp, log, sin, cos, tan
from add import *

class Diapason(Exception):
    def __init__(self, text):
        self.text = text


def f(point, funf):
    x, y = point
    return eval(funf)


def nelder_mead(fu, x1, x2, x3, maxiter=70, alpha=1, beta=0.5, gamma=2,):
    # initialization
    v1 = Vector(x1[0], x1[1])
    v2 = Vector(x2[0], x2[1])
    v3 = Vector(x3[0], x3[1])

    for i in range(maxiter):
        adict = {v1: f(v1.c(), fu), v2: f(v2.c(), fu), v3: f(v3.c(), fu)}
        points = sorted(adict.items(), key=lambda x: x[1])

        b = points[0][0]
        g = points[1][0]
        w = points[2][0]

        mid = (g + b) / 2

        # reflection
        xr = mid + alpha * (mid - w)
        if f(xr.c(), fu) < f(g.c(), fu):
            w = xr
        else:
            if f(xr.c(), fu) < f(w.c(), fu):
                w = xr
            c = (w + mid) / 2
            if f(c.c(), fu) < f(w.c(), fu):
                w = c
        if f(xr.c(), fu) < f(b.c(), fu):

            # expansion
            xe = mid + gamma * (xr - mid)
            if f(xe.c(), fu) < f(xr.c(), fu):
                w = xe
            else:
                w = xr
        if f(xr.c(), fu) > f(g.c(), fu):

            # contraction
            xc = mid + beta * (w - mid)
            if f(xc.c(), fu) < f(w.c(), fu):
                w = xc

        # update points
        v1 = w
        v2 = g
        v3 = b
    return b


def inputs(fu, x1, x2, x3, count):
    xk = nelder_mead(fu, x1, x2, x3, count)
    print("Function value = %s" % f(xk.c(), fu))
    print("Best poits is: %s" % (xk))
    return [xk.c(), f(xk.c(), fu)]



