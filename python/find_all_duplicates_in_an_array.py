# ======================================
# LeetCode Problem: find all duplicates in an array
# Language: python
# Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Synced by: LinkCode
# Date: 10/8/2026, 6:25:36 PM
# ======================================


class Solution(object):
    def findDuplicates(self, nums):
        result = []
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        for key, value in dict.items():
            if value > 1:
                result.append(key)
        return result
            

