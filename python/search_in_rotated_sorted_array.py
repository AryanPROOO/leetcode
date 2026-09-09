# ======================================
# LeetCode Problem: search in rotated sorted array
# Language: python
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Synced by: LinkCode
# Date: 9/9/2026, 6:38:41 PM
# ======================================


class Solution(object):
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1