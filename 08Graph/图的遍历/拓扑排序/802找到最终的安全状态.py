class Solution:
    # 拓扑排序，graph 中包含所有顶点的有向边关系（包括无边顶点）
    def topologicalSortingKahn(self, graph: dict):
        indegrees = {u: 0 for u in graph}   # indegrees 用于记录所有节点入度
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1           # 统计所有节点入度
        
        # 将入度为 0 的顶点存入集合 S 中
        S = collections.deque([u for u in indegrees if indegrees[u] == 0])
        
        while S:
            u = S.pop()                     # 从集合中选择一个没有前驱的顶点 0
            for v in graph[u]:              # 遍历顶点 u 的邻接顶点 v
                indegrees[v] -= 1           # 删除从顶点 u 出发的有向边
                if indegrees[v] == 0:       # 如果删除该边后顶点 v 的入度变为 0
                    S.append(v)             # 将其放入集合 S 中
        
        res = []
        for u in indegrees:
            if indegrees[u] == 0:
                res.append(u)
        
        return res
        
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph_dict = {u: [] for u in range(len(graph))}

        for u in range(len(graph)):
            for v in graph[u]:
                graph_dict[v].append(u)     # 逆序建图

        return self.topologicalSortingKahn(graph_dict)
