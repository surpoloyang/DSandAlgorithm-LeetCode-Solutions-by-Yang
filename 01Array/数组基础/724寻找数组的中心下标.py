class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        S = sum(nums)
        preSum = 0
        for i in range(N):
            if preSum == S - preSum - nums[i]:
                return i
            preSum += nums[i]
        return -1