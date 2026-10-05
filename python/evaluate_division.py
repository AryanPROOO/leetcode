# ======================================
# LeetCode Problem: evaluate division
# Language: python
# Link: https://leetcode.com/problems/evaluate-division/
# Synced by: LinkCode
# Date: 10/5/2026, 6:32:22 PM
# ======================================


from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)
        for (a,b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1/value))

        def dfs(current, target, visited):
            if current == target:
                return 1.0
            visited.add(current)
            for neighbor, weight in graph[current]:
                if neighbor in visited:
                    continue
                result = dfs(neighbor, target, visited)
                if result != -1.0:
                    return weight* result
            return -1.0
        result = []
        for a, b in queries:
            if a not in graph or b not in graph:
                result.append(-1.0)
            else:
                result.append(dfs(a,b, set()))
        return result