import pytest
from functions import f1b

@pytest.mark.parametrize(
        "arr, ans",
        [
            ([1, 2], [2]),
            ([12, 23, 23], [23, 23]),
            ([23324, 24323135, 82983], [24323135, 82983]),
            ([-23324, -24323135, -82983], [-24323135, -82983]),
            ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0])
        ]
)

def test_f1a(arr, ans):
    assert f1b(arr) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test_f1b.py'])