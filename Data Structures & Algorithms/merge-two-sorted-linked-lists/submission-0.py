# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        p1 = list1
        p2 = list2

        while (p1 or p2):
            curr.next = ListNode()
            if p1 is not None and p2 is not None:
                curr.next = ListNode()
                if p1.val < p2.val:
                    curr.next.val = p1.val
                    p1 = p1.next
                
                else:
                    curr.next.val = p2.val
                    p2 = p2.next
            
            elif p1 is not None:
                curr.next.val = p1.val
                p1 = p1.next
            
            else:
                curr.next.val = p2.val
                p2 = p2.next
            
            curr = curr.next
        
        return dummy.next
