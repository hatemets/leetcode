from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        # Swap the pointers to the next nodes (next points to prev and vice versa)
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

d: ListNode = ListNode(4)
c: ListNode = ListNode(3, d)
b: ListNode = ListNode(2, c)
a: ListNode = ListNode(1, b)

sol = Solution()
print(sol.reverseList(a).next.next.next.val)
