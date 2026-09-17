# ======================================
# LeetCode Problem: sort colors
# Language: python
# Link: https://leetcode.com/problems/sort-colors/
# Synced by: LinkCode
# Date: 9/17/2026, 1:34:42 PM
# ======================================


class Solution(object):
    def sortColors(self, nums):

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1