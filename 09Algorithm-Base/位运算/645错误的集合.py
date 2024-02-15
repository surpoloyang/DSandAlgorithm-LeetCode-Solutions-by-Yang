class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total = sum(range(1, len(nums)+1))
        num = total - sum(set(nums))
        diff = total - sum(nums)
        return [num-diff, num]