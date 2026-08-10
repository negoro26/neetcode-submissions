# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        while current: 
            stack.append(current)
            current = current.next

        if not stack:
            return None

        new_head = stack.pop()
        current = new_head
            
        while stack:
            next_node = stack.pop()
            current.next = next_node
            current = next_node

        current.next = None

        return new_head


