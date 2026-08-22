# ======================================
# LeetCode Problem: first missing positive
# Language: python
# Link: https://leetcode.com/problems/first-missing-positive/
# Synced by: LinkCode
# Date: 8/22/2026, 11:37:59 PM
# ======================================


class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1