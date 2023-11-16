from random import randint
import pytest
from app import ArmashSort

@pytest.mark.parametrize(
        "l", 
        [
            (10),
            (100),
            (1000),
            (10000),
            (100000)
        ]
)

def test(l):
    arr = []
    for i in range(10):
        arr.append(str(randint(0, 2)))
        if arr[-1] == '2':
            arr[-1] = '3'
    assert ArmashSort(arr) == ''.join(sorted(arr, reverse=True))

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])