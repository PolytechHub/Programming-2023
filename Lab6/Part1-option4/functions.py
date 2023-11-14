from collections import Counter
from random import randint
from math import inf

def get_array(len=100, mini=-1000, maxi=1000):
    return [randint(mini, maxi) for _ in range(len)]

def get_num(mini=-1000, maxi=1000):
    return randint(mini, maxi)

def f1a(arr: list, a: int):
    minindex = -1
    minval = inf
    for i, val in enumerate(arr):
        evens = 0
        product = 1
        for digit in str(abs(val)):
            digit = int(digit)
            if digit % 2 == 0:
                evens += 1
            product *= digit
        if (evens == a or product % val == 0) and minval > val:
            minindex = i
            minval = val
    return minindex

def f1b(arr, k1, k2):
    def validate(n):
        # Ищем элемент с минимальной суммой делителей, включая 1
        # Иначе почти всегда будет 0
        b = abs(n)
        s = 0
        for i in range(1, n):
            if n % i == 0:
                s += i
        return s == n

    nums = []
    for i in arr[k1:k2+1]:
        if validate(i):
            nums.append(i)
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)

def f2(arr):
    c = Counter(arr)
    m = -inf
    for i, j in c.items():
        if j < 3:
            m = max(i, m)
    return m