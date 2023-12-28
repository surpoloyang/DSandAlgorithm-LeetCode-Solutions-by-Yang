class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size == 1:
            return nums
        for i in range(1, size):
            insert_i = i
            # for j in range(i-1, -1, -1):
            #     if nums[j] > nums[i]:
            #         insert_i = j
            # nums.insert(insert_i, nums.pop(i))

            j = i-1
            while j >=0 and nums[j] > nums[i]:
                insert_i = j
                j -= 1
            nums.insert(insert_i, nums.pop(i))