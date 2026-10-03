# ======================================
# LeetCode Problem: sqrtx
# Language: python
# Link: https://leetcode.com/problems/sqrtx/
# Synced by: LinkCode
# Date: 10/3/2026, 4:41:55 PM
# ======================================


import math
class Solution(object):
    def mySqrt(self, x):
        if x <2:
            return x
        left = 1
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid  == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

