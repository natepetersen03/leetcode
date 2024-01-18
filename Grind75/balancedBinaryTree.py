'''
Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.height(root) >= 0
    def height(self, node):
        if not node:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)
        # checking for any imbalanced nodes in future or if current node is imbalanced
        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1
        else:
            return 1 + max(left, right)