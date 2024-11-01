#https://leetcode.com/problems/insertion-sort-list/?envType=problem-list-v2&envId=sorting
#Code:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        current = head 

        while current:
            prev = dummy  
            next_node = current.next 
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            current.next = prev.next
            current = next_node

        return dummy.next  
def to_linked_list(lst):
    dummy = ListNode()
    tail = dummy
    for value in lst:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
