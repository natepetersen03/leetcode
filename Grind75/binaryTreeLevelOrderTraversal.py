'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # base case
        if not root:
            return []
        level = 0
        queue = [(root, level)]
        currNodes = []
        returnList = []
        # general idea is pushing the level and node to queue, and if new level is reached add the prev level to return val
        while queue:
            node, lev = queue.pop(0)
            if lev == level + 1:
                returnList.append(currNodes)
                currNodes = []
                level += 1
            currNodes.append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        returnList.append(currNodes)
        return returnList