#!/usr/bin/python3

import pymprog as MP
from solve_lp import solve_lp
from lp_cfg import *


if __name__ == '__main__':
    lp = MP.begin('LP1994UG')
    c = [(20 - 130/60 - 40/60, 30 - 190/60 - 58/60), 0]
    A = [(13, 19),
            (20, 29),
            (1, 0)]
    b = [(40*60, 'lte'),
            (35*60, 'lte'),
            (10, 'gte')]
    lp.verbose(True)
    solve_lp(MAXIMIZE, lp, c, A, b)
    lp.sensitivity()
    lp.end()
