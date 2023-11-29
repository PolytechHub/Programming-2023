#!/usr/bin/env python3

import pytest
from auto import Auto

@pytest.mark.parametrize(
        "func, data, ans",
        [
            ("go_to_city", [100, 100], True),
            ("distance_to_point", [100000, -100000], 141183.97),
            ("cost_of_trip", "*[[5, -5], 1001]", 33238.63),
            ("time_of_trip_with_max_speed", [112, -112], 1.01),
            ("price_loss", "*[]", 900000)
        ]
)
def test(func, data, ans):
    auto = Auto()
    assert round(eval(f'auto.{func}({data})'), 2) == ans
    
if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])