# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        carry = _sum = 0
        
        while (l1 or l2):
            if l1 and l2:
                _sum = (l1.val + l2.val + carry)
                l1, l2 = l1.next, l2.next
            
            elif not l1:
                _sum = (l2.val + carry)
                l2 = l2.next
            
            else:
                _sum = (l1.val + carry)
                l1 = l1.next
              
            carry = (_sum // 10)
            _sum %= 10
            node.next = ListNode(val = _sum)

            node = node.next

        if carry:
            node.next = ListNode(val = carry)
  
        return dummy.next


        
