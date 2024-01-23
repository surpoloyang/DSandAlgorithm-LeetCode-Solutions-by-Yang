class Solution:
    def reverseWords(self, s: str) -> str:
        slow, fast = 0, 0
        while fast < len(s):
            if s[fast] == ' ':
                s = s[:slow] + s[slow:fast][::-1] + s[fast:]
                slow = fast + 1
            fast += 1
        return s[:slow] + s[slow:][::-1]