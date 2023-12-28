class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = dict()
        cnt = 0
        while right < len(s):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            cnt = max(cnt, right - left + 1)
            right += 1
        return cnt