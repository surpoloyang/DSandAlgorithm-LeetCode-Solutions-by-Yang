class Solution:
    def convertToBase7(self, num: int) -> str:
        s = ''
        if num == 0:
            return '0'
        signal = '-' if num < 0 else ''
        num = abs(num)
        while num:
            num, m = divmod(num, 7)
            s = str(m) + s
        s = signal + s
        return s