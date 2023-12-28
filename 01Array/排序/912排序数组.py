class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 计数排序
        nums_min, nums_max = min(nums), max(nums)
        size = nums_max - nums_min + 1
        counts = [0 for i in range(size)]
        for n in nums:
            counts[n-nums_min] += 1
        i = 0
        j = 0
        while j < len(nums):
            if counts[i] > 0:
                nums[j] = i + nums_min
                counts[i] -= 1
                j += 1
            else:
                i += 1

        nums.sort()
        return nums

        # 堆排序
        # return heapq.nsmallest(len(nums), nums)

        # 希尔排序
        # size = len(nums)
        # gap = size // 2

        # while gap > 0:
        #     for i in range(gap, size):
        #         insert_i = i
        #         j = i - gap
        #         while j >= 0 and nums[j] > nums[i]:
        #             insert_i = j
        #             j -= gap
        #         nums.insert(insert_i, nums.pop(i))
        #     gap //= 2
        # return nums

                 