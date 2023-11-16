from math import inf
import pytest
from functions import f2

@pytest.mark.parametrize(
        "arr, k, C, ans",
        [
            ([1, 2, 3, 4, 5], 0, 5, 4),
            ([1, 2, 3, 4, 5], 0, 2, -inf),
            ([134718241234, 12341234, 12341, 1234234], 1, 4, 1234234),
            ([9139192381923, 123123123123, 8193480182043, 12348198430134], 0, 3, -inf),
            ([0, 0, 0], 0, 7, -inf)
        ]
)

def test_f1a(arr, k, C, ans):
    assert f2(arr, k, C) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test_f2.py'])