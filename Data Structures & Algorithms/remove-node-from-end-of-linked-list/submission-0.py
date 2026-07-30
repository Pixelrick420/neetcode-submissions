class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        dummy = ListNode()
        dummy.next = head
        node = head

        while node:
            size += 1
            node = node.next
        
        node = dummy
        for _ in range(size - n):
            node = node.next

        node.next = node.next.next
        return dummy.next