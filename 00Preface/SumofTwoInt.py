nums, k = [3,2,1,5,6,4], 2

nums_min, nums_max = min(nums), max(nums)
size = nums_max-nums_min+1
counts = [0 for _ in range(size)]
for n in nums:
    counts[n-nums_min] += 1
idx = 0
j = 0
while j < len(nums):
    if counts[idx] > 0:
        nums[j] = idx + nums_min
        counts[idx] -= 1
        j += 1
    else:
        idx += 1
print(nums[-k])