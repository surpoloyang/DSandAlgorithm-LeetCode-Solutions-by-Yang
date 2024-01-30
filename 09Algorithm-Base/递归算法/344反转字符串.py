class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.recursion(s, 0, len(s)-1)

    def recursion(self, s, left, right):
        if left >= right:
            return
        self.recursion(s, left+1, right-1)
        s[left], s[right] = s[right], s[left]
        
        