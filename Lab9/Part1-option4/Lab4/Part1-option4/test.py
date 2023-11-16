import pytest
from app import computeFunction

@pytest.mark.parametrize(
        "test, ans",
        [
            (-10,2),
            (-6,0),
            (0,-3),
            (3,0),
            (6,3)
        ]
)
def test(test, ans):
    assert computeFunction(test) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])