# ======================================
# LeetCode Problem: remove nth node from end of list
# Language: python
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Synced by: LinkCode
# Date: 10/15/2026, 5:57:16 PM
# ======================================


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        remove_index = length - n

        if remove_index == 0:
            return head.next

        curr = head

        for i in range(remove_index - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head