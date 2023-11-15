from math import inf

def calsDevs(n):
    if n == 0:
        return inf
    n = abs(n)
    iter = 1
    devs = 0
    while iter*iter <= n:
        if n % iter == 0:
            devs += 2
        if iter*iter == n:
            devs -= 1
        iter += 1
    return devs

def f1(matrix):
    prods = []
    for row in matrix:
        prod = 1
        ok = True
        for elem in row:
            prod *= elem
            if elem < 0:
                ok = False
                break
        prods.append(prod if ok else None)
    return prods

def f2(matrix, C):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = True if calsDevs(matrix[i][j]) > C else False
    return matrix