class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        ssets = []
        for num in range(1 << size):
            sset = []
            for idx in range(size):
                if num >> idx & 1:
                    sset.append(nums[idx])
            ssets.append(sset)
        return ssets
