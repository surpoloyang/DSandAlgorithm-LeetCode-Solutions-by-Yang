# # 递归
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.fib(n - 1) + self.fib(n - 2)


# 动态规划
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
