# ======================================
# LeetCode Problem: remove duplicates from sorted array
# Language: python
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Synced by: LinkCode
# Date: 8/22/2026, 3:01:54 PM
# ======================================


class Solution(object):
    def removeDuplicates(self, nums):
        num = []
        k = 0
        for i in range (1, len(nums)):
            if nums[i] != nums[k]:
                k+=1
                nums[k] = nums[i]
            else:
                pass
        return k+1
            

