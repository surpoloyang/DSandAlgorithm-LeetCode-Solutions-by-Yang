class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        # while right >= left:
        #     mid = left + (right-left) // 2
        #     if target < nums[mid]:
        #         right = mid - 1
        #     elif target > nums[mid]:
        #         left = mid + 1
        #     else:
        #         return mid
        # return -1
        while left < right:
            mid = left + (right-left) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left if target == nums[left] else -1