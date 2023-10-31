import pytest
from app import computeFunction

def test1():
    assert computeFunction(-10) == 2

def test2():
    assert computeFunction(-6) == 0

def test3():
    assert computeFunction(0) == -3

def test4():
    assert computeFunction(3) == 0

def test5():
    assert computeFunction(6) == 3

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])