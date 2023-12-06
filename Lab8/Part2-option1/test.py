import pytest
from PyQt6.QtCore import QDate
from app import sieve

@pytest.mark.parametrize(
        "items, border, ratio, threshhold, ans",
        [
            (
                [{'name': "test1", 'date': QDate(2023, 12, 6), 'count': 99, 'cost': 999}],
                QDate(2030, 12, 6), 10, 1,
                [{'name': 'test1', 'cost': 899.1, 'count': 99, 'sum': 89010.9, 'date': QDate(2023, 12, 6)}]
            ),
            (
                [{'name': "test2", 'date': QDate(2031, 12, 6), 'count': 99, 'cost': 999}],
                QDate(2030, 12, 6), 10, 1,
                []
            ),
            (
                [{'name': "test3", 'date': QDate(2023, 12, 6), 'count': 100, 'cost': 999}],
                QDate(2030, 12, 6), 10, 1,
                [{'name': 'test3', 'cost': 899.1, 'count': 100, 'sum': 89910, 'date': QDate(2023, 12, 6)}]
            ),
            (
                [{'name': "test4", 'date': QDate(2023, 12, 6), 'count': 99, 'cost': 1000}],
                QDate(2030, 12, 6), 10, 1,
                [{'name': 'test4', 'cost': 900, 'count': 99, 'sum': 89100, 'date': QDate(2023, 12, 6)}]
            ),
            (
                [{'name': "test5", 'date': QDate(2023, 12, 6), 'count': 99, 'cost': 999}],
                QDate(2030, 12, 6), 10, 999,
                [{'name': 'test5', 'cost': 999, 'count': 99, 'sum': 98901, 'date': QDate(2023, 12, 6)}]
            )
        ]
)
def test(items, border, ratio, threshhold, ans):
    assert sieve(items, border, ratio, threshhold) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])