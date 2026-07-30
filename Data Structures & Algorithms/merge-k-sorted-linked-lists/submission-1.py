class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        merged = dummy
        heap = []
        k = len(lists)
        for i in range(k):
            node = lists[i]
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        
        while heap:
            val = heapq.heappop(heap)
            merged.next = ListNode(val)
            merged = merged.next
    
        return dummy.next