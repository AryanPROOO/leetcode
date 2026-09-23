# ======================================
# LeetCode Problem: combination sum
# Language: python
# Link: https://leetcode.com/problems/combination-sum/
# Synced by: LinkCode
# Date: 9/23/2026, 7:50:07 PM
# ======================================


class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        def backtrack (start, target, current):
            if target <0:
                return []
            if target == 0:
                result.append(current[:])
                return
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, target - candidates[i], current)
                current.pop()

        backtrack(0,target,[])
        return result
