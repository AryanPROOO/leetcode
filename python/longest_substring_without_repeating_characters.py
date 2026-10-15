# ======================================
# LeetCode Problem: longest substring without repeating characters
# Language: python
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Synced by: LinkCode
# Date: 10/15/2026, 10:54:47 PM
# ======================================


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left =0
        max_length=0
        char=set()
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left+=1

            char.add(s[right])
            max_length=max(max_length, right-left+1)
        return max_length