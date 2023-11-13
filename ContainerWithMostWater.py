'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maximum = min([height[0], height[1]])
        a = 0
        b = len(height) - 1
        while (a < b):
            minHeight = min([height[a], height[b]])
            area = (b - a) * minHeight
            maximum = max([maximum, area])
            if (minHeight == height[a] and minHeight == height[b]):
                a += 1
                b -= 1
            elif minHeight == height[a]:
                while (height[a] <= minHeight):
                    a += 1
            else:
                while (height[b] <= minHeight):
                    b -= 1
        return maximum
