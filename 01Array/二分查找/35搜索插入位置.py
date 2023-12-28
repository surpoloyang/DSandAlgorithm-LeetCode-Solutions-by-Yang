# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, 2**31-1
        while left <= right:
            
            if guess(n) == 0:
                return n
            elif guess(n) == -1:
                right = n-1
            else:
                left = n+1
            n = left + (right-left) // 2
            
        