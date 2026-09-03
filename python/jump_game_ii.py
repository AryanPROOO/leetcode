# ======================================
# LeetCode Problem: jump game ii
# Language: python
# Link: https://leetcode.com/problems/jump-game-ii/
# Synced by: LinkCode
# Date: 9/3/2026, 1:44:28 PM
# ======================================


class Solution(object):
    def jump(self, nums):
        currentend = 0
        jump = 0
        farthest = 0
        for i in range (len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if i == currentend:
                jump+=1
                currentend = farthest
        return jump
        