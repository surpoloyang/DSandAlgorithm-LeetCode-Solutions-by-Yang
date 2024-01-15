class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans = []
        # for i in nums1:
        #     stack = []
        #     idx = nums2.index(i)
        #     ans.append(-1)
        #     for j in range(idx, len(nums2)):
        #         if nums2[j] > i:
        #             ans[-1] = nums2[j]
        #             break
        #     return ans
        ans = []
        stack = []
        hashmap = {}    #{nums中的当前元素值: 下一个更大的元素值}
        for num in nums2:
            while stack and stack[-1] < num:
                hashmap[stack.pop()] = num
            stack.append(num)
            
        for num in nums1:
            ans.append(hashmap.get(num, -1))
        return ans