# ======================================
# LeetCode Problem: palindrome partitioning
# Language: python
# Link: https://leetcode.com/problems/palindrome-partitioning/
# Synced by: LinkCode
# Date: 9/24/2026, 3:17:17 AM
# ======================================


class Solution(object):
    def partition(self, s):
        result = []
        def backtrack(start, current):
            if start == len(s):
                result.append(current[:])
                return
            for end in range(start, len(s)):
                subs = s[start:end+1]
                if subs == subs[::-1]:
                    current.append(subs)
                    backtrack(end+1, current)
                    current.pop()
        backtrack(0, [])
        return result

        