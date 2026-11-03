# ======================================
# LeetCode Problem: find missing and repeated values
# Language: python
# Link: https://leetcode.com/problems/find-missing-and-repeated-values/
# Synced by: LinkCode
# Date: 11/3/2026, 6:05:52 PM
# ======================================


class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        result=[]
        seen=set()
        missing =0
        n=len(grid)
        for i in grid:
            for j in i:
                if j in seen: 
                    result.append(j)
                else:
                    seen.add(j)
        for i in range(1,n*n+1):
            if i not in seen:
                missing=i
                result.append(missing)
                break
        return result