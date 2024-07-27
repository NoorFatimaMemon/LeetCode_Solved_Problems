"""Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1: Input: root = [1,2,2,3,4,4,3], Output: true
Example 2: Input: root = [1,2,2,null,3,null,3], Output: false
 
Constraints: The number of nodes in the tree is in the range [1, 1000]. -100 <= Node.val <= 100
Follow up: Could you solve it both recursively and iteratively?"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def LRNodes(left, right):
            if not left and not right: 
                return True
            if not left or not right: 
                return False
            
            return (left.val == right.val and 
                    LRNodes(left.left, right.right) and 
                    LRNodes(left.right, right.left))
        return LRNodes(root.left, root.right)



# Example 1: Input: root = [1,2,2,3,4,4,3], Output: true
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.left = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

x = Solution()
out1 = x.isSymmetric(root1)
print(out1)  # Output: [1, 3, 2]
