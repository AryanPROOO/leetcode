# ======================================
# LeetCode Problem: intersection of two arrays
# Language: python
# Link: https://leetcode.com/problems/intersection-of-two-arrays/
# Synced by: LinkCode
# Date: 10/6/2026, 5:24:53 PM
# ======================================


class Solution(object):
    def intersection(self, nums1, nums2):
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if nums1[i] in result:
                        continue
                    else:
                        result.append(nums1[i])
                else:
                    continue
        return result            