# ======================================
# LeetCode Problem: remove duplicates from sorted array
# Language: python
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Synced by: LinkCode
# Date: 11/3/2026, 5:08:37 PM
# ======================================



class Solution(object):
    def removeDuplicates(self, nums):
        left = 0
        right = left + 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right+=1
            else:
                left+=1
                nums[left]=nums[right]

        return left + 1
