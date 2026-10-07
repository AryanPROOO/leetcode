# ======================================
# LeetCode Problem: permutations
# Language: python
# Link: https://leetcode.com/problems/permutations/
# Synced by: LinkCode
# Date: 10/7/2026, 7:27:24 AM
# ======================================


class Solution(object):
    def permute(self, nums):
        result = []
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            for j in range(start, len(nums)):
                nums[start], nums[j] = nums[j], nums[start]
                backtrack(start + 1)
                nums[start], nums[j] = nums[j], nums[start]
        backtrack(0)
        return result