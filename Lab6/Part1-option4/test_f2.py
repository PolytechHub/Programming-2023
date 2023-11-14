from math import inf
import pytest
from functions import f2

@pytest.mark.parametrize(
        "arr, ans",
        [
            ([1, 2, 3], 3),
            ([1, 2, 3, 3, 3], 2),
            ([-1, -1, -100, 0], 0),
            ([13412341, 7812734, 13412341, 124314241, 13412341], 124314241),
            ([0, 0, 0, 0, 0, 0, 0, 0], -inf)
        ]
)

def test_f2(arr, ans):
    assert f2(arr) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test_f2.py'])