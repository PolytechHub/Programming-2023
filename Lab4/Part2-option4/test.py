import pytest
from app import antilLog10

@pytest.mark.parametrize(
        "test, ans", 
        [
            (12.12, 1318256738556.4048),
            (89.91, 8.128305161640929e+89),
            (-8.11, 0.0000000078),
            (-71.17, 0),
            (100, int('1'+'0'*100))
        ]
)

def test(test, ans):
    assert round(antilLog10(12.12), 10) == 1318256738556.4048

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])