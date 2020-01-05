#!/usr/bin/python3

import pymprog as mp
import numpy as np
import math

def mp_solve_lp(model_name, obj, c, vars_cnt, A, b, b_condition):
    P = mp.begin(model_name)
    P.verbose(True)

    x = P.var('x', vars_cnt)
    
    if (obj == 'max'):
        P.maximize(sum(c[i]*x[i] for i in range(len(x))))
    else:
        P.minimize(sum(c[i]*x[i] for i in range(len(x))))

    for i in range(len(b)):
        if (b_condition[i] == 'gt'):
            sum(A[i][j]*x[j] for j in range(len(x))) >= b[i]
        elif (b_condition[i] == 'eq'):
            sum(A[i][j]*x[j] for j in range(len(x))) == b[i]
        else:
            sum(A[i][j]*x[j] for j in range(len(x))) <= b[i]

    P.solve()
    P.sensitivity()
    coef_range_lb = {}
    coef_range_ub = {}
    cons_range_lb = {}
    cons_range_ub = {}
    cols = P.get_num_cols()
    idx = 0
    for val in P._viter(range(1, cols+1)):
        coef_range_lb[idx] = val[5]
        coef_range_ub[idx] = val[6]
        idx = idx + 1

    rows = P.get_num_rows()
    idx = 0
    for val in P._citer(range(1, rows+1)):
        cons_range_lb[idx] = val[6]
        cons_range_ub[idx] = val[7]
        idx = idx + 1

    #print(coef_range_lb, coef_range_ub)
    #print(cons_range_lb, cons_range_ub)
    obj_val = P.get_obj_val()

    P.end()
    return obj_val,coef_range_lb, coef_range_ub

# Primal: 01
def mp_obj_fn_01():

    # Set up obj coef c
    c = (5, 4.5, 6)
    # Set up constraints
    A = [   (6, 5, 8),
            (10, 20, 10),
            (1, 0, 0) ]
    # Set up RHS of the constraints
    b = (60, 150, 8)
    b_condition = ('lt', 'lt', 'lt')

    mp_solve_lp('P01', 'max', c, len(c), A, b, b_condition)

    return

def mp_obj_fn_02():
    c = [3, 5]
    A = [ [1, 0], [0, 2], [3,2] ]
    b = [4, 12, 18]
    b_condition = ['lt', 'lt', 'lt']

    fval = 0
    cval = 0
    obj_val,lb,ub = mp_solve_lp('P02', 'max', c, len(c), A, b, b_condition)
    cntr = 0
    fval = obj_val
    cval = c
    while(cntr < 5):
        for idx in range(len(c)):
            if (type(ub[idx]) is float):
                if (ub[idx] >= 1.79769e+308):
                    continue
                if (ub[idx] == 0):
                    continue
                c[idx] = c[idx] + ub[idx]
        obj_val,lb,ub = mp_solve_lp('P02', 'max', c, len(c), A, b, b_condition)
        if (obj_val == math.inf):
            break
        cval = c
        fval = obj_val
        cntr = cntr + 1

    print("Final Value: {}, Obj Val:{}".format(fval, cval))

    return

if __name__ == '__main__':
    #mp_obj_fn_01()
    mp_obj_fn_02()
