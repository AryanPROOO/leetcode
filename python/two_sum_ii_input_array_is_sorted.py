# ======================================
# LeetCode Problem: two sum ii input array is sorted
# Language: python
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Synced by: LinkCode
# Date: 9/23/2026, 10:12:06 PM
# ======================================


class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        while left<right:
            total = numbers[left]+numbers[right]
            if total == target:
                return[left+1, right+1]
            elif total > target:
                right-=1
            else:
                left+=1