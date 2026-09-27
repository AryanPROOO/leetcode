# ======================================
# LeetCode Problem: rearrange array elements by sign
# Language: python
# Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/
# Synced by: LinkCode
# Date: 9/27/2026, 6:37:24 PM
# ======================================


class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        for i in nums:
            if i > 0:
                pos.append(i)
            if i < 0:
                neg.append(i)
        ans = []
        for j in range(len(pos)):
            ans.append(pos[j])
            ans.append(neg[j])
        
        return ans