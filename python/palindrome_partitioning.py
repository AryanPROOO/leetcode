# ======================================
# LeetCode Problem: palindrome partitioning
# Language: python
# Link: https://leetcode.com/problems/palindrome-partitioning/
# Synced by: LinkCode
# Date: 9/24/2026, 3:16:14 AM
# ======================================


class Solution(object):
    def partition(self, s):
        result = []
        def backtrack(start, current):
            if start == len(s):
                result.append(current[:])
                return
            for end in range(start, len(s)):
                substring = s[start:end+1]
                if substring == substring[::-1]:
                    current.append(substring)
                    backtrack(end+1, current)
                    current.pop()
        backtrack(0, [])
        return result

        