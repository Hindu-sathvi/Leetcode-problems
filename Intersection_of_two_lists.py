#https://leetcode.com/problems/intersection-of-two-linked-lists/?envType=problem-list-v2&envId=two-pointers
#Code:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        lenA = get_length(headA)
        lenB = get_length(headB)
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
        
