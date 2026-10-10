# ======================================
# LeetCode Problem: can make arithmetic progression from sequence
# Language: python
# Link: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
# Synced by: LinkCode
# Date: 10/10/2026, 3:32:13 PM
# ======================================


class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-1):
                if arr[j] > arr[j+1]:
                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
        diff = arr[1]-arr[0]
        for i in range(1,n-1):
            if arr[i+1] - arr[i] != diff:
                return False
        return True

