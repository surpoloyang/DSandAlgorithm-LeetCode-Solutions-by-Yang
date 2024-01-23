class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        idx = 0
        size = len(s)
        while idx < size//2:
            s[idx], s[-1-idx] = s[-1-idx], s[idx]
            idx += 1