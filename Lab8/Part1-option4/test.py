import pytest
from function import change_register

@pytest.mark.parametrize(
        "string, ans",
        [
            ("КаЖдЫй ОхОтНиК", 'кАжДыЙ оХоТнИк'),
            ("Macbook Air", 'mACBOOK aIR'),
            ("iPhone 11", 'IpHONE 11'),
            ("Модная кружка от Softline", 'мОДНАЯ КРУЖКА ОТ sOFTLINE'),
            ("Ящик Боржоми", 'яЩИК бОРЖОМИ')
        ]
)
def test(string, ans):
    assert change_register(string) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])