class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        numset = set([i**2 for i in range(2, n+1)])
        for a in range(3, n):
            for b in range(a+1, n):
                if a**2 + b**2 in numset:
                    cnt += 2
        return cnt