"""Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1: Input: root = [1,null,2,3], Output: [1,3,2]
Example 2: Input: root = [], Output: []
Example 3: Input: root = [1], Output: [1]
 
Constraints: The number of nodes in the tree is in the range [0, 100]. -100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: 
            return []
        out = self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        return out

# Example 1: Input: root = [1,null,2,3]
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

"""# Example 2: Input: root = []
root2 = None

# Example 3: Input: root = [1]
root3 = TreeNode(1)"""

x = Solution()
out1 = x.inorderTraversal(root1)
print(out1)  # Output: [1, 3, 2]

"""out2 = x.inorderTraversal(root2)
print(out2)  # Output: []

out3 = x.inorderTraversal(root3)
print(out3)  # Output: [1]"""
