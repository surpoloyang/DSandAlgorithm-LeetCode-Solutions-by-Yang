class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        left, size = 0, len(lst)
        while left < size//2:
            lst[left], lst[-1-left] = lst[-1-left], lst[left]
            left += 1
        return ' '.join(lst)