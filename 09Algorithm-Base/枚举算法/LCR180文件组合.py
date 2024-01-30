class Solution:
    def fileCombination(self, target: int):
        numlist = [i for i in range(1, target//2+2)]
        ans = []
        low, fast = 0, 1
        size = len(numlist)
        while fast < size:
            while sum(numlist[low:fast+1]) <= target and fast < size:
                if sum(numlist[low:fast+1]) == target:
                    ans.append(numlist[low:fast+1])
                fast += 1
            low += 1
            fast = low + 1
        return ans