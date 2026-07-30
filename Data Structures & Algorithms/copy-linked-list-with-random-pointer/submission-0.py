"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None : None}
        node = head
        while node:
            nodes[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            nodes[node].next = nodes[node.next]
            nodes[node].random = nodes[node.random]
            node = node.next
            
        return nodes[head]

