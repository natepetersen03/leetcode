'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        '''
        LOGIC:
        backed by stack which is always increasing.
        for every index, pop from stack until you reach a height that is less than the height at that index
        for every popped element, the height is the popped element's height * the width of the histogram up to but not including
        the current element.
        once the array has been iterated through, pop all elements off the stack using the same logic.
        '''
        # stack should be always increasing
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            #pop from stack until pushing the new index would result in the stack increasing
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(height * (i - index), maxArea)
                start = index
            stack.append((start, h))
        while stack:
            index, height = stack.pop()
            width = len(heights) - index
            maxArea = max(height * width, maxArea)
        return maxArea