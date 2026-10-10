# ======================================
# LeetCode Problem: next permutation
# Language: python
# Link: https://leetcode.com/problems/next-permutation/
# Synced by: LinkCode
# Date: 10/10/2026, 1:05:36 PM
# ======================================



class Solution(object):
    def nextPermutation(self, nums):
        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = reversed(nums[i + 1:])
