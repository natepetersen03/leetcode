'''
104. Maximum Depth of Binary Tree
Easy
12.3K
204
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # recurse to helper
        return self.maxDepthHelper(root, 1)
    def maxDepthHelper(self, root, height):
        if not root:
            return 0
        return max(height, self.maxDepthHelper(root.left, height + 1), self.maxDepthHelper(root.right, height + 1))