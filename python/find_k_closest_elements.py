# ======================================
# LeetCode Problem: find k closest elements
# Language: python
# Link: https://leetcode.com/problems/find-k-closest-elements/
# Synced by: LinkCode
# Date: 10/2/2026, 11:33:15 PM
# ======================================


class Solution(object):
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr)-k
        while left < right:
            mid = (left + right)// 2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]