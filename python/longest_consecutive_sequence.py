# ======================================
# LeetCode Problem: longest consecutive sequence
# Language: python
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Synced by: LinkCode
# Date: 11/15/2026, 12:15:36 AM
# ======================================


class Solution(object):
    def longestConsecutive(self, nums):
        count=1
        max_count =1
        nums_set = sorted(set(nums))
        if not nums_set:
            return 0
        for i in range(len(nums_set)-1):
            nums_next= nums_set[i]+1
            if nums_set[i+1] == nums_next:
                count+=1
            else:
                count=1
            max_count = max(count, max_count)
        return max_count