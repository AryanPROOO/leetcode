# ======================================
# LeetCode Problem: intersection of two arrays
# Language: python
# Link: https://leetcode.com/problems/intersection-of-two-arrays/
# Synced by: LinkCode
# Date: 10/6/2026, 5:26:06 PM
# ======================================


class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1)& set(nums2))          