"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self, node, visitedNode):
        if node in visitedNode:
            return visitedNode[node]
        clone_node = Node(node.val, [])
        visitedNode[node] = clone_node
        
        for neighbor in node.neighbors:
            clone_node.neighbors.append(self.dfs(neighbor, visitedNode))
        
        return clone_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visitedNode = dict()
        return self.dfs(node, visitedNode)   
                