import pytest
from app import func

@pytest.mark.parametrize(
        "x, y, z, ans",
        [
            (1, 2, 3, 33.54),
            (0, 0, 1, 0),
            (3223, 13143, 1341, 443683369960.43),
            (-12342, -12134, -1, 0.13),
            (0, 0, 0, 0)
        ]
)
def test(x, y, z, ans):
    assert round(func(x, y, z), 2) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])