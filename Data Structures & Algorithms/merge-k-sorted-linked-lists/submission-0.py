class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        finished = 0
        dummy = ListNode(0)
        merged = dummy

        while (finished < k):
            curVal, curList = float('inf'), -1
            for i in range(k):
                if lists[i] and lists[i].val < curVal:
                    curVal = lists[i].val
                    curList = i

            lists[curList] = lists[curList].next
            if not lists[curList]:
                finished += 1
            merged.next = ListNode(curVal)
            merged = merged.next
        return dummy.next

        