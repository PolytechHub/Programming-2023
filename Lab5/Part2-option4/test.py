from random import randint
import pytest
from app import ArmashSort

def test1():
    arr = []
    for i in range(10):
        arr.append(str(randint(0, 2)))
        if arr[-1] == '2':
            arr[-1] = '3'
    assert ArmashSort(arr) == ''.join(sorted(arr, reverse=True))

def test2():
    arr = []
    for i in range(100):
        arr.append(str(randint(0, 2)))
        if arr[-1] == '2':
            arr[-1] = '3'
    assert ArmashSort(arr) == ''.join(sorted(arr, reverse=True))

def test3():
    arr = []
    for i in range(1000):
        arr.append(str(randint(0, 2)))
        if arr[-1] == '2':
            arr[-1] = '3'
    assert ArmashSort(arr) == ''.join(sorted(arr, reverse=True))

def test4():
    arr = []
    for i in range(10000):
        arr.append(str(randint(0, 2)))
        if arr[-1] == '2':
            arr[-1] = '3'
    assert ArmashSort(arr) == ''.join(sorted(arr, reverse=True))

def test5():
    arr = []
    for i in range(100000):
        arr.append(str(randint(0, 2)))
        if arr[-1] == '2':
            arr[-1] = '3'
    assert ArmashSort(arr) == ''.join(sorted(arr, reverse=True))

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])