# ======================================
# LeetCode Problem: valid perfect square
# Language: python
# Link: https://leetcode.com/problems/valid-perfect-square/
# Synced by: LinkCode
# Date: 10/10/2026, 3:55:25 PM
# ======================================


class Solution(object):
    def isPerfectSquare(self, num):
        if num < 0:
            return False

        if num < 2:
            return True

        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2

            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
