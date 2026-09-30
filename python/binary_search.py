# ======================================
# LeetCode Problem: binary search
# Language: python
# Link: https://leetcode.com/problems/binary-search/
# Synced by: LinkCode
# Date: 9/30/2026, 6:19:39 PM
# ======================================


class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1
