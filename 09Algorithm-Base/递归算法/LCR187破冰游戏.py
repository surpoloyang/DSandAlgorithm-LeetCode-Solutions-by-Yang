class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
        numlist = [i for i in range(num)]
        return self.recursion(numlist, 0, target)
    def recursion(self, numlist, idx, target):
        size = len(numlist)
        if size == 1:
            return numlist[0]
        idx = (idx + target - 1) % size
        numlist.pop(idx)
        return self.recursion(numlist, idx, target)
        # 此题解很好
        # https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solutions/178431/jie-shi-di-tui-gong-shi-di-gui-die-dai-sui-bian-xi 
        