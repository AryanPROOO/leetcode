# ======================================
# LeetCode Problem: 3sum closest
# Language: python
# Link: https://leetcode.com/problems/3sum-closest/
# Synced by: LinkCode
# Date: 8/19/2026, 5:58:30 PM
# ======================================


class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        for i in range (len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                total = nums[i]+nums[left] + nums[right]
                if abs(total - target) < abs(result - target):
                    result = total
                if total < target:
                    left += 1

                elif total > target:
                    right -= 1

                else:
                    return total
        return result


        