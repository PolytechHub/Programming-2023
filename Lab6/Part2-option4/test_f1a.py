import pytest
from functions import f1a

@pytest.mark.parametrize(
        "arr, ans",
        [
           ([4, 6, 7], [4, 6, 5]),
           ([78232, 818234, 651971], [78232, 818234, 516145]),
           ([812938, 643369, 9881234], [812938, 3779180, 9881234]),
           ([-812938, -643369, -9881234], [-812938, -3779180, -9881234]),
           ([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0])
        ]
)

def test_f1a(arr, ans):
    assert list(map(int, f1a(arr))) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test_f1a.py'])