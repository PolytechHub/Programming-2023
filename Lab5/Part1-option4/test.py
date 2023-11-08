import pytest
from app import computeFunction

@pytest.mark.parametrize(
        "X, A, ans",
        [
            (-10, 30, -139.11),
            (10, 60, -382.68),
            (-1000, 100, -33157766.20),
            (100, 1, -10001.3),
            (0, 0, 0)
        ]
)

def test(X, A, ans):
    assert round(computeFunction(X, A), 2) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])