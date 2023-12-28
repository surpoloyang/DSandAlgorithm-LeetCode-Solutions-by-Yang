class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # tem = 0
        # cnt = 0
        # while True:
        #     if nums[tem] == 0:
        #         nums.append(nums.pop(tem))
        #         cnt += 1
        #     else:
        #         tem += 1
        #     if tem == len(nums)-cnt:
        #         break
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
        return nums

