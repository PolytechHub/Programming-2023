import pytest
from auto import Auto

@pytest.mark.parametrize(
        "func, data, ans",
        [
            ("go_to_city", 100, True),
            ("distance_to_point", 100000, 99663),
            ("cost_of_trip", "*[1001, 5]", 332),
            ("time_of_trip_with_max_speed", 112, 0.9),
            ("price_loss", "*[]", 900000)
        ]
)
def test(func, data, ans):
    auto = Auto()
    assert eval(f'auto.{func}({data})') == ans
    
if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])