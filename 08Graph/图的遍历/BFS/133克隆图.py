"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
import collections
class Solution:
#    BFS
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visited = dict()
        queue = collections.deque([])
        visited[node] = Node(node.val, [])
        queue.append(node)
        while queue:
            node_u = queue.popleft()
            for neighbor in node_u.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = Node(neighbor.val, [])
                visited[node_u].neighbors.append(visited[neighbor])
        return visited[node]