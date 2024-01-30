class Solution:
    def isPrime(self, x: int) -> bool:
        for i in range(2, int(pow(x, 0.5))+1):
            if x % i == 0:
                return False
        return True
    
    def countPrimes(self, n: int) -> int:
        cnt = 0
        for i in range(2, n):
            if self.isPrime(i):
                cnt += 1
        return cnt