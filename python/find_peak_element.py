# ======================================
# LeetCode Problem: find peak element
# Language: python
# Link: https://leetcode.com/problems/find-peak-element/
# Synced by: LinkCode
# Date: 9/25/2026, 1:25:29 PM
# ======================================


class Solution(object):
    def findPeakElement(self, nums):
        left = 0
        right =len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid]<nums[mid+1]:
                left = mid +1
            else:
                right = mid
        return left
