from typing import Optional
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid: Optional[ListNode] = ListNode(head.val, head.next)
        mi: int = 0
        i = 0

        while head:
            k = math.ceil(i / 2)
            j = mi
            while j < k:
                mid = ListNode(mid.next.val, mid.next.next)
                j += 1
            mi = k

            head = head.next
            i += 1
            print(i, mi)

        return mid



f = ListNode(6)
e = ListNode(5, f)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

sol: Solution = Solution()
print(sol.middleNode(a).val)
