# ======================================
# LeetCode Problem: top k frequent elements
# Language: python
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Synced by: LinkCode
# Date: 9/15/2026, 6:17:25 PM
# ======================================


class Solution(object):
    def topKFrequent(self, nums, k):
        dict = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        for i in range(k):
            most_freq = max(dict, key=dict.get)
            result.append(most_freq)
            del dict[most_freq]
        return result