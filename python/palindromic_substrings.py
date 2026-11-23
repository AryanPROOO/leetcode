# ======================================
# LeetCode Problem: palindromic substrings
# Language: python3
# Link: https://leetcode.com/problems/palindromic-substrings/
# Synced by: LinkCode
# Date: 11/23/2026, 11:03:18 PM
# ======================================


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def expand(left, right):
            nonlocal count
            while (left >= 0 and right < len(s) and s[left]==s[right]):
                count+=1
                left-=1
                right+=1
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        return count