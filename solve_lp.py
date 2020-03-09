#!/usr/bin/python3

import pymprog as MP
from lp_cfg import *

def solve_lp(op, lp, c, A, b):
    x = lp.var('x', len(c[0]))
    if (op == MAXIMIZE):
        lp.maximize(c[1] + sum(c[0][i]*x[i] for i in range(len(c[0]))))
    else:
        lp.miniimize(c[1] + sum(c[0][i]*x[i] for i in range(len(c[0]))))

    for i in range(len(A)):
        if ('lte' == b[i][1]):
            sum(A[i][j]*x[j] for j in range(len(c[0]))) <= b[i][0]
        elif('gte' == b[i][1]):
            sum(A[i][j]*x[j] for j in range(len(c[0]))) >= b[i][0]
        else:
            sum(A[i][j]*x[j] for j in range(len(c[0]))) == b[i][0]

    lp.solve()
    return

