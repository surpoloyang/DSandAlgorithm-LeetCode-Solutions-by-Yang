class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        maps = {}
        for i in nums:
            if i in maps:
                return True
            else:
                maps[i] = 1
        return False
