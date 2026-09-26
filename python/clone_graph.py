# ======================================
# LeetCode Problem: clone graph
# Language: python
# Link: https://leetcode.com/problems/clone-graph/
# Synced by: LinkCode
# Date: 9/26/2026, 4:11:18 PM
# ======================================


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        map = {}
        def dfs(node):
            if node in map:
                return map[node]
            clone = Node(node.val)
            map[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)
            