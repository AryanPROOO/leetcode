# ======================================
# LeetCode Problem: container with most water
# Language: python
# Link: https://leetcode.com/problems/container-with-most-water/
# Synced by: LinkCode
# Date: 8/18/2026, 3:53:57 PM
# ======================================


class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxi_mum = 0
        while left < right:
            length = min(height[left], height[right])
            width = right - left
            area = length * width
            maxi_mum = max(maxi_mum, area)
            if height[left] <height[right]:
                left+=1
            else:
                right-=1
        return maxi_mum

        