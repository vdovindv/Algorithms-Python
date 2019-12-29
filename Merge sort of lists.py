# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l_res = ListNode(None) #result list
        cur = l_res
        while (l1 or l2): #while pointer of l1 or l2 are not NULL
            el_to_add = None
            if l2 is None or l1 is not None and l1.val<l2.val:
                el_to_add = l1.val
                l1 = l1.next
            else:
                el_to_add = l2.val
                l2 = l2.next
            #Create new Node to add in result list
            next_node = ListNode(el_to_add)
            cur.next = next_node
            cur = next_node
        return l_res.next