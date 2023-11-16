import pytest
from functions import f1b

@pytest.mark.parametrize(
        "arr, k1, k2, ans",
        [
           ([6, 28, 496], 0, 2, 176.67),
           ([31, 6, 23423, -134134, 81234, 11, 28, 496, 77], 1, 7, 176.67),
           ([81784, 141234, 123234, 12431312, 12434, 13434], 3, 5, 0),
           ([8128, 247823, 24234, 1265346], 0, 3, 8128),
           [[0, 0, 0, 0, 0], 0, 0, 0]
        ]
)

def test_f1b(arr, k1, k2, ans):
    assert round(f1b(arr, k1, k2), 2) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test_f1b.py'])