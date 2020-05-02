# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: return l1 or l2 #if one of l1 or l2 lists are empty we'll return not empty list, if both are empty, return empty list
        
        ans = None #result list
        prev = None 
        
        cur1 = l1 #setting up starting
        cur2 = l2 #                   values for vars that will iterate by lists
        add_1 = 0
        
        
        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            
            digit = val1 + val2 + add_1
            add_1 = int(digit / 10)
            
            node = ListNode(digit % 10)
            if not ans: 
                ans = node
            else:
                prev.next = node
            
            prev = node    
            if cur1 : cur1 = cur1.next
            if cur2 : cur2 = cur2.next
        
        if add_1:
            prev.next = ListNode(1)
        return ans
