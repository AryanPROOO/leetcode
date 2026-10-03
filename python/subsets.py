# ======================================
# LeetCode Problem: subsets
# Language: python
# Link: https://leetcode.com/problems/subsets/
# Synced by: LinkCode
# Date: 10/3/2026, 1:46:34 PM
# ======================================


class Solution(object):
    def subsets(self, nums):
        result = []
        def backtrack(start, current):
            result.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i+1, current)

                current.pop()
        backtrack(0, [])
        return result