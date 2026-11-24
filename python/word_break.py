# ======================================
# LeetCode Problem: word break
# Language: python3
# Link: https://leetcode.com/problems/word-break/
# Synced by: LinkCode
# Date: 11/24/2026, 4:49:27 PM
# ======================================


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordset=set(wordDict)
        result = [False]*(len(s)+1)
        result[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if result[j] and s[j:i] in wordset:
                    result[i] = True
                    break 
        return result[len(s)]