# ======================================
# LeetCode Problem: remove element
# Language: python
# Link: https://leetcode.com/problems/remove-element/
# Synced by: LinkCode
# Date: 11/3/2026, 5:29:47 PM
# ======================================


class Solution(object):
    def removeElement(self, nums, val):
        left =0
        right=0
        while right<len(nums):
            if nums[right]!=val:
                nums[left]=nums[right]
                left+=1
            right+=1
        return left
