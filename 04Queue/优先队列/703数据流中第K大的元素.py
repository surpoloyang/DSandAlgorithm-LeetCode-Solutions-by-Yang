import heapq

class KthLargest:

    def __init__(self, k: int, nums: list):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums)>k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums)<self.k:
            heapq.heappush(self.nums, val)
        elif val>self.nums[0]: # 如果在堆里的值小于加进来的值，则替换堆中的最小值为val
            heapq.heapreplace(self.nums, val)
        return self.nums[0] # 返回堆顶元素就是第k大的元素


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)