# ======================================
# LeetCode Problem: running sum of 1d array
# Language: python
# Link: https://leetcode.com/problems/running-sum-of-1d-array/
# Synced by: LinkCode
# Date: 10/10/2026, 3:11:22 PM
# ======================================


class Solution(object):
    def runningSum(self, nums):
        result = []
        current = 0
        for i in range(len(nums)):
            current = current + nums[i]
            result.append(current)
        return result