# CHRIS FELLI, 2019
# A positive integer is magical if it is divisible by either A or B.
# Return the N-th magical number. Since the answer may be very large, 
# return it modulo 10^9 + 7.

class Solution:
    def __init__(self, N=0, A=0, B=0):
        self.N = N
        self.A = A  
        self.B = B

    # This functions at smaller numbers...
    def nthMagicalNumberNaive(self, N: int, A: int, B: int) -> int:
        L = []
        C = I = 0
        # Edge Case
        if (N==1):
            return min(A, B)
        # Main Case
        while C<N:
            if((I%A==0 or I%B==0)and I!=0):
                L.append(I)
                C+=1
                I+=1
            else:
                I+=1
        return L[C-1]
    
    def gcd(self, x, y):
	    while y > 0:
		    x, y = y, x % y
	    return x

    def lcm(self, x, y):
	    return x*y//self.gcd(x,y)

    def nthMagicalNumber(self, N, A, B):
	    temp = self.lcm(A,B)
	    seq = {}
	    for i in range(1,temp//A+1):
	    	seq[i*A] = 1
	    for i in range(1,temp//B+1):
	    	seq[i*B] = 1
	    cand = sorted([key for key, value in seq.items()])
	    ans = ((N-1)//len(cand))*cand[-1] + cand[N%len(cand)-1]
	    return ans % (10**9+7)

# Testcases
test = Solution()
print(test.nthMagicalNumber(1, 2, 3))
print(test.nthMagicalNumber(4, 2, 3))
print(test.nthMagicalNumber(5, 2, 4))
print(test.nthMagicalNumber(3, 6, 4))
print(test.nthMagicalNumber(3, 8, 3))
print(test.nthMagicalNumber(1000000000,40000,40000))