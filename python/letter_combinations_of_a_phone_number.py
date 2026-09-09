# ======================================
# LeetCode Problem: letter combinations of a phone number
# Language: python
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Synced by: LinkCode
# Date: 9/9/2026, 6:12:36 PM
# ======================================


class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []

        def backtrack (ind, path):
            if ind == len(digits):
                result.append(path)
                return 
            for i in map[digits[ind]]:
                backtrack(ind+1, path + i)
        backtrack(0,"")
        return result