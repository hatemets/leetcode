from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head

        vals: list[int] = []

        while head:
            vals.append(head.val)
            head = head.next

        newHead: ListNode = ListNode(vals[-1])
        curr: ListNode = newHead

        for i in range(len(vals)):
            if i == 0:
                curr = ListNode(vals[-(i + 1)])
                newHead.next = curr
            else:
                curr.next = ListNode(vals[-(i + 1)])
                curr = curr.next

        return newHead.next

e: ListNode = ListNode(5)
d: ListNode = ListNode(4, e)
c: ListNode = ListNode(3, d)
b: ListNode = ListNode(2, c)
a: ListNode = ListNode(1, b)

sol = Solution()
print(sol.reverseList(a).val)
