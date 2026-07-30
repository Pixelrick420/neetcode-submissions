class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while(slow and fast and fast.next):
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False