import pytest


def is_palindrome(x: str) -> bool:
    """is x a palindrome"""
    x = x.replace(' ', '')
    x = x.lower()
    if len(x) < 1:
        return True
    else:
        if x[0] == x[-1]:
            x = x[1:-1]
            return(is_palindrome(x))
        else:
            return False


def test_ufo_tofu():
    """ufo tofu and some appropriate permutations"""
    assert is_palindrome("ufo tofu") is True
    assert is_palindrome("UFO tofu") is True
    assert is_palindrome("UFOTOFU") is True
    assert is_palindrome("ufo tofu") is True
    assert is_palindrome("u  FOt O fu") is True


def test_race_car():
    """race car and some appropriate permutations"""
    assert is_palindrome("race car") is True
    assert is_palindrome("racecar") is True
    assert is_palindrome("RACECAR") is True
    assert is_palindrome("rA C E Ca r") is True
    assert is_palindrome("r  AcEcA  r") is True


def test_hello_world():
    """Hello, world!"""
    assert is_palindrome("Hello, world!") is False
    assert is_palindrome("helloworld") is False


def test_weird_al_yankovic_bob():
    """
    little did Weird Al Yankovic know he created the perfect test case
    """
    yankovic_array = ["I man am regal a German am I",
                      "Never odd or even",
                      "If I had a hifi",
                      "Madam Im Adam",
                      "Too hot to hoot",
                      "No lemons no melon",
                      "Too bad I hid a boot",
                      "Lisa Bonet ate no basil",
                      "Warsaw was raw",
                      "Was it a car or a cat I saw",
                      "Rise to vote sir",
                      "Do geese see god",
                      "Do nine men interpret Nine men I nod",
                      "Rats live on no evil star",
                      "Wont lovers revolt now",
                      "Race fast safe car",
                      "Pas a sap",
                      "Ma is as selfless as I am",
                      "May a moody baby doom a yam",
                      "Ah Satan sees Natasha",
                      "No devil lived on",
                      "Lonely Tylenol",
                      "Not a banana baton",
                      "No X in Nixon",
                      "O stone be not so",
                      "O Geronimo no minor ego",
                      "Naomi I moan",
                      "A Toyotas a Toyota",
                      "A dog a panic in a pagoda",
                      "Oh no Don Ho",
                      "Nurse I spy gypsies run",
                      "Senile felines",
                      "Now I see bees I won",
                      "UFO tofu",
                      "We panic in a pew",
                      "Oozy rat in a sanitary zoo",
                      "God A red nugget A fat egg under a dog",
                      "Go hang a salami Im a lasagna hog"]
    for i in yankovic_array:
        assert is_palindrome(i) is True


def test_empty():
    with pytest.raises(AttributeError):
        is_palindrome(None)


def test_9():
    with pytest.raises(AttributeError):
        is_palindrome(9)
