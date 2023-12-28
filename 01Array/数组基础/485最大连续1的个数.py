class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = ''.join(str(i) for i in nums)
        strlist = s.split('0')
        return max(strlist).count('1')