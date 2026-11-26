# ======================================
# LeetCode Problem: palindromic substrings
# Language: python3
# Link: https://leetcode.com/problems/palindromic-substrings/
# Synced by: LinkCode
# Date: 11/26/2026, 8:28:50 PM
# ======================================


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        def expand(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        return count