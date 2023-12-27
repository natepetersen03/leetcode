'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Logic: left and right pointers, both converging on eachother.
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        totalArea = 0
        while left < right:
            #if the left pointer < right pointer
            if height[left] < height[right]:
                if height[left] > leftMax:
                    #new maximum on the left, water cannot be held in this position
                    leftMax = height[left]
                else:
                    #if there is a greater column on both right/left, we can put water here
                    #we know we can because leftMax is greater and the right pointer is greater
                    totalArea += leftMax - height[left]
                left += 1
            #same logic but in reverse
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    totalArea += rightMax - height[right]
                right -= 1
        return totalArea