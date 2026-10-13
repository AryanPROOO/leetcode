# ======================================
# LeetCode Problem: add two numbers
# Language: python
# Link: https://leetcode.com/problems/add-two-numbers/
# Synced by: LinkCode
# Date: 10/14/2026, 12:45:09 AM
# ======================================


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total // 10
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
