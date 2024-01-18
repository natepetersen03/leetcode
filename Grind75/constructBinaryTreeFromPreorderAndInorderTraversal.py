'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #General idea is to split it into subtrees. If preorder[0] = inorder[0],
        #there is no left subtree, so it will not continue constucting to the left.
        #The same can be said the other way around: if preorder[0] = inorder[-1],
        #there is no right subtree so construction will only occur to the left.
        #this continues recursively until there are no more nodes to construct.
        if inorder:
            root = TreeNode(preorder.pop(0))
            index = inorder.index(root.val)
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root