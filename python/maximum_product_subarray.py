# ======================================
# LeetCode Problem: maximum product subarray
# Language: python3
# Link: https://leetcode.com/problems/maximum-product-subarray/
# Synced by: LinkCode
# Date: 11/27/2026, 5:05:47 PM
# ======================================


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            result = max(result, max_product)

        return result