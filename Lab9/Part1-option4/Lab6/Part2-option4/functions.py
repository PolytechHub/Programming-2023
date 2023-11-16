from random import randint
from math import inf

def get_array(len=100, mini=-1000, maxi=1000, strings=False):
    if strings:
        return [str(randint(mini, maxi)) for _ in range(len)]
    return [randint(mini, maxi) for _ in range(len)]

def get_num(mini=-1000, maxi=1000):
    return randint(mini, maxi)

def f1a(arr):
    def gs(n):
        n = abs(n)
        s = 0
        for i in range(2, n):
            if n % i == 0:
                s += i
        return s
    mini = 0
    for i, val in enumerate(arr):
        if gs(val) < gs(arr[mini]):
            mini = i
    arr[mini] = sum(arr) / len(arr)
    return arr

def f1b(arr):
    new_arr = []
    for i, val in enumerate(arr):
        s = 0
        p = 1
        for j in str(abs(val)):
            j = int(j)
            s += j
            p *= j
        if (i != 0 and p % i == 0) or (s != 0 and val % s != 0) or val == 0:
            new_arr.append(val)
    return new_arr

def f2(arr, k, C):
    arr = arr[k+1:]
    m = -inf
    for val in arr:
        if val % C != 0 and val % 2 == 0:
            m = max(m, val)
    return m