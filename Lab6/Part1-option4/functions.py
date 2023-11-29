from collections import Counter
from random import randint
from math import inf

def get_array(len=100, mini=-1000, maxi=1000, strings=False):
    if strings:
        return [str(randint(mini, maxi)) for _ in range(len)]
    return [randint(mini, maxi) for _ in range(len)]

def get_num(mini=-1000, maxi=1000):
    return randint(mini, maxi)

def f1a(arr: list, a: int):
    minindex = -1
    minval = inf
    for i, val in enumerate(arr):
        if val == 0: 
            if minval > val:
                minindex = i
                minval = val
            continue
        evens = 0
        product = 1
        for digit in str(abs(val)):
            digit = int(digit)
            if digit % 2 == 0:
                evens += 1
            product *= digit
        if (evens == a or product != 0 and val % product == 0) and minval > val:
            minindex = i
            minval = val
    return minindex

def f1b(arr, k1, k2):
    def validate(n):
        # Ищем элементы с суммой делителей, включая 1 = самому элементу
        # Они же «совершенные числа»
        # Иначе почти всегда ничего не найдем
        n = abs(n)
        s = 1
        i = 2
        while i*i <= n:
            if n % i == 0:
                s += i + n//i
                if i*i == n:
                    s -= i
            i += 1
        return s == n

    summ = 0
    cnt = 0
    for i in arr[k1:k2+1]:
        if validate(i):
            summ += i
            cnt += 1
    if cnt == 0:
        return 0
    return summ / cnt

def f2(arr):
    c = Counter(arr)
    m = -inf
    for i, j in c.items():
        if j < 3:
            m = max(i, m)
    return m