import pytest
from functions import calsDevs, f1, f2

# @pytest.mark.parametrize(
#         "matrix, ans",
#         [
#             ([[1]], [1]),
#             ([[2, -2], [2, 2]], [None, 4]),
#             ([[3, -3, 3], [-3, 3, 3], [3, 3, 3]], [None, None, 27]),
#             ([[-4, -4, -4, 3], [-4, 4, 4, 4], [4, 4, 4, 4], [4, 4, -4, -4]], 
#                 [None, None, 256, None]),
#             ([[-5, -5, -5, 5], [-5, -5, 5, -5, 5], [5, 5, 5, 5, 5], [5, 5, -5, 5],
#               [5, 5, 5, 5, 5]], 
#                 [None, None, 3125, None, 3125])
#         ]
# )
# def test_f1(matrix, ans):
#     assert f1(matrix) == ans

@pytest.mark.parametrize(
        "matrix, C, ans",
        [
            ([[1]], 1, [[False]]),
            ([[2, 3], [3, 7]], 3, [[False, False], [False, False]]),
            ([[2423, 123], [23, 23]], 3, [[False, True], [False, False]]),
            ([[24231234, -123], [2323, 2323234]], 4, [[True, False], [False, False]]),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 999999, [[True, True, True],
                [True, True, True], [True, True, True]])
        ]
)
def test_f2(matrix, C, ans):
    assert f2(matrix, C) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])