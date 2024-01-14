class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        size = len(s)
        op = '+'
        index = 0
        while index < size:
            if s[index] == ' ':
                index += 1
                continue
            if s[index].isdigit():
                num = s[index]
                while index + 1 < size and s[index + 1].isdigit():
                    index += 1
                    num += s[index]
                num = int(num)
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    top = stack.pop()
                    stack.append(top * num)
                elif op == '/':
                    top = stack.pop()
                    stack.append(int(top / num))
            elif s[index] in '+-*/':
                op = s[index]
            index += 1
        return sum(stack)

# s = "14-3/2"
# sol = Solution()
# sol.calculate(s)