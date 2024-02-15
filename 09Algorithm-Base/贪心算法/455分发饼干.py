class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        indexg, indexs = 0, 0
        cnt = 0
        sizeg = len(g)
        sizes = len(s)
        while indexg < sizeg and indexs < sizes:
            if g[indexg] <= s[indexs]:
                cnt += 1
                indexg += 1
                indexs += 1
            else:
                indexs += 1
        return cnt