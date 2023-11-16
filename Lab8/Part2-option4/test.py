import pytest
from app import cals

@pytest.mark.parametrize(
        "k, p, items, ans",
        [
            (15, 10, [{'cat': 102, 'name': "Товар 5", 'count': 60, 'cost': 15}],
                [{'cat': 102, 'name': "Товар 5", 'count': 60, 'cost': 15, 'discount': 90}]),
            (15, 10, [{'cat': 101, 'name': "Товар 1", 'count': 5, 'cost': 100}], []),
            (90, 25, [{'cat': 112, 'name': "Товар 7", 'count': 12, 'cost': 98}], []),
            (87, 25, [{'cat': 162, 'name': "Товар 12", 'count': 73, 'cost': 21}], []),
            (337, 27, [{'cat': 123, 'name': "Товар 75", 'count': 87, 'cost': 228}], [])
        ]
)
def test(k, p, items, ans):
    assert cals(k, p, items) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])