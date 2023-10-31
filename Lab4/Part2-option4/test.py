import pytest
from app import antilLog10

def test1():
    assert round(antilLog10(12.12), 10) == 1318256738556.4048

def test2():
    assert round(antilLog10(89.91), 10) == 8.128305161640929e+89

def test4():
    assert round(antilLog10(-8.11), 10) == 0.0000000078

def test4():
    assert round(antilLog10(-71.17), 10) == 0.0000000000

def test5():
    assert round(antilLog10(100), 10) == int('1'+'0'*100)

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])