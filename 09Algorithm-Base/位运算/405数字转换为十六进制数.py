class Solution:
    def toHex(self, num: int) -> str:
        #如果是0直接返回"0"
        if num == 0:
            return "0"
        #十六进制字符串
        CONV = "0123456789abcdef"
        s = ''
        #因为是32位机器，所以是8个F
        num = num & 0xFFFFFFFF
        while num:
            #从右至左，每4个bit位进行与操作，得到该十六进制的字符表示
            s = CONV[num & 0XF] + s
            #每次右移4位
            num = num >> 4
        #结果取反序返回
        return s
