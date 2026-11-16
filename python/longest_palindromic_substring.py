# ======================================
# LeetCode Problem: longest palindromic substring
# Language: python3
# Link: https://leetcode.com/problems/longest-palindromic-substring/
# Synced by: LinkCode
# Date: 11/16/2026, 5:43:42 PM
# ======================================



class Solution(object):
    def longestPalindrome(self, s):
        list_s = list(s)
        res = [""]
        def even(left, right):
            while left >= 0 and right < len(list_s) and list_s[left] == list_s[right]:
                if right - left + 1 > len(res[0]):
                    res[0] = s[left:right+1]
                left -= 1
                right += 1
        for mid in range(len(list_s)):
            even(mid, mid)
            even(mid - 1, mid)
        return res[0]
