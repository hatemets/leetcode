from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# a = TreeNode(5)
# b = TreeNode(3, a)
# x = TreeNode(6)
# f = TreeNode(4, None, x)
# c = TreeNode(2, b, f)
# d = TreeNode(1, c)
# print(Solution().diameterOfBinaryTree(d))

# a = TreeNode(5)
# b = TreeNode(4)
# c = TreeNode(2, a, b)
# d = TreeNode(3)
# e = TreeNode(1, c, d)
# print(Solution().diameterOfBinaryTree(e))

c = TreeNode(2)
b = TreeNode(3)
a = TreeNode(1, b, c)
print(Solution().maxDepth(a))
