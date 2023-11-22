import pytest
from vector import Vector

@pytest.mark.parametrize(
        "func, data, ans",
        [
            ("get_x_angle", [], 0),
            ("get_y_angle", [], 90),
            ("get_angle_between", [Vector(0, 1)], 90),
            ("get_scalar_product", [Vector(0, 1)], 0),
            ("get_vector_product", [Vector(0, 1)], 1)
        ]
)
def test(func, data, ans):
    vector = Vector(1, 0)
    assert round(eval(f'vector.{func}')(*data), 2) == ans
    
if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])