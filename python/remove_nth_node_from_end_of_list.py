# ======================================
# LeetCode Problem: remove nth node from end of list
# Language: python
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Synced by: LinkCode
# Date: 10/15/2026, 6:20:44 PM
# ======================================


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        remove_item=length-n
        if remove_item==0:
            return head.next
        curr = head
        for i in range(remove_item-1):
            curr=curr.next
        curr.next = curr.next.next
        return head