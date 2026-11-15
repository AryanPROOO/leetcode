# ======================================
# LeetCode Problem: longest consecutive sequence
# Language: python
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Synced by: LinkCode
# Date: 11/15/2026, 1:24:52 PM
# ======================================


class Solution(object):
    def longestConsecutive(self, nums):
        max_count =0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                count = 1
                current = num
                while current+1 in nums_set:
                    current+=1
                    count+=1
                max_count = max(max_count, count)
        return max_count