class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def backtrack(nums, index):
            res.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()
        backtrack(nums, 0)
        return res