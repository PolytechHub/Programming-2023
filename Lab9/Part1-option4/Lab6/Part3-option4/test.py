import pytest
from app import checkShot

@pytest.mark.parametrize(
        "x, y, r, ans",
        [
            (2, 2, 5, True),
            (1, -1, 2, False),
            (-2, -2, 3, True),
            (-1, 1, 10, True),
            (0, 0, 0, True)
        ]
)

def test(x, y, r, ans):
    assert checkShot(x, y, r) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])