#!/usr/bin/python3

import pymprog as mp
import numpy as np

# Primal & Dual: 01
def mp_pd_01():

    P = mp.begin('Primal of PD_01')
    x = P.var('x', 3)
    # Max c.x
    # s.t.
    # Ax <= b
    
    # Set up obj coef c
    c = (5, 4.5, 6)
    # Set up constraints
    A = [   (6, 5, 8),
            (10, 20, 10),
            (1, 0, 0) ]
    # Set up RHS of the constraints
    b = (60, 150, 8)

    P.verbose(True)
    # Plug in objective fn
    P.maximize(sum(c[i]*x[i] for i in range(len(x))))
    # Plug in constraints
    for i in range(len(b)):
        sum(A[i][j]*x[j] for j in range(len(x))) <= b[i]
    
    P.solve()

    # Dual part
    D = mp.begin('Dual of PD_01')
    D.verbose(True)
    # Min b.y
    # s.t.
    # Transpose(A)*y >= c
    y = D.var('y', len(b))

    # Use numpy to get the transpose(A)
    # 1. Convert A to numpy matrix
    mA = np.matrix(A)
    # 2. B is transpose of A
    mB = mA.transpose()
    # 3. Convert to list to feed into PyMProg
    B = mB.tolist()

    # now we have b, c, y, transpose(A) to run the Dual
    D.minimize(sum(b[i]*y[i] for i in range(len(y))))
    # contraints part
    for i in range(len(c)):
        sum(B[i][j]*y[j] for j in range(len(y))) >= c[i]

    D.solve()
    
    print("")
    print("Report of Primal_01")
    P.sensitivity()
    print("Report of Dual_01")
    D.sensitivity()

    P.end()
    D.end()

    return

if __name__ == '__main__':
    mp_pd_01()
