#!/usr/bin/python3

import pymprog as MP
from lp_cfg import *
from solve_lp import solve_lp


if __name__ == '__main__':
    # Max/Min W = Cx
    # s.t.
    # Ax [lte, gte, e] b

    lp = MP.begin('LP1997UG')
    lp.verbose(True)

    c = [(1, 1), 30 - 75 + 90 - 95]
    A = [(50, 24),
            (30 , 33),
            (1, 0),
            (0, 1)]
    b = [(40 * 60, 'lte'), 
            (35 * 60, 'lte'),
            (75 - 30, 'gte'),
            (95 - 90, 'gte')]

    solve_lp(MAXIMIZE, lp, c, A, b)

    lp.sensitivity()
    lp.end()
    
