class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        index = 0
        size = len(s)
        while index < size:
            if not stack:
                stack.append(s[index])
            else:
                if stack[-1] == s[index]:
                    stack.pop()
                else:
                    stack.append(s[index])
            index += 1
        return "".join(stack)
                