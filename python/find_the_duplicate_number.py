# ======================================
# LeetCode Problem: find the duplicate number
# Language: python
# Link: https://leetcode.com/problems/find-the-duplicate-number/
# Synced by: LinkCode
# Date: 10/6/2026, 6:05:56 PM
# ======================================


class Solution(object):
    def findDuplicate(self, nums):
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = True
            else:
                return nums[i]