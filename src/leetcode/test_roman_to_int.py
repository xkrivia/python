def romantoint(x):
    """convert roman numeral to integer"""
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    working = 0
    for i in range(0, len(x) - 1):
        if roman[x[i]] < roman[x[i+1]]:
            working -= roman[x[i]]
        else:
            working += roman[x[i]]
    return working + roman[x[-1]]


def test_i():
    """I is 1"""
    assert romantoint('I') == 1


def test_ii():
    """II is 2"""
    assert romantoint('II') == 2


def test_iii():
    """III is 3"""
    assert romantoint('III') == 3


def test_iv():
    """IV is 4"""
    assert romantoint('IV') == 4


def test_iiii():
    """IIII is 4 for illiterate romans"""
    assert romantoint('IIII') == 4


def test_v():
    """V is 5"""
    assert romantoint('V') == 5


def test_x():
    """X is 10"""
    assert romantoint('X') == 10


def test_l():
    """L is 50"""
    assert romantoint('L') == 50


def test_c():
    """C is 100"""
    assert romantoint('C') == 100


def test_d():
    """D is 500"""
    assert romantoint('D') == 500


def test_m():
    """M is 1000"""
    assert romantoint('M') == 1000
