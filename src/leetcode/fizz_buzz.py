class Solution:
    def fizzBuzz(self, n):
        fb = []
        for x in range(1,n+1):
            if x % 3 == 0 and x % 5 == 0:
                track = 'FizzBuzz'
            elif x % 5 == 0:
                track = 'Buzz'
            elif x % 3 == 0:
                track = 'Fizz'
            else:
                track = str(x)
            fb.append(track)
        return fb


def test_xv():
    return Solution().fizzBuzz(15)
