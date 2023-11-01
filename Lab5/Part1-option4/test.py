import pytest
from app import computeFunction

def test1():
    assert round(computeFunction(-10, 30), 2) == -139.11

def test2():
    assert round(computeFunction(10, 60), 2) == -382.68

def test3():
    assert round(computeFunction(-1000, 100), 2) == -33157766.20

def test4():
    assert round(computeFunction(1000, 1), 2) == -1000287.22

def test5():
    assert round(computeFunction(0, 0), 2) == 0.00

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])