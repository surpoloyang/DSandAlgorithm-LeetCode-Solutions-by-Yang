class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        size = len(position)
        odds = sum(x & 1 for x in position)
        return odds if odds < size-odds else size-odds
# 偶数都可以移到2，奇数都可以移到1，所以只有1->2 or 2->1这一步会有cost，
# 所以计算奇偶数个数就可以知道答案