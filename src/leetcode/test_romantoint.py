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
