'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #base case: rotated back to start position
        if nums[0] < nums[len(nums)-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        midpoint = len(nums) / 2
        #essentially binary search, must use other nodes as points of reference. 
        while (left < right):
            if nums[left] < nums[right]:
                break
            #1: case where first point in an array is greater than the center
            if nums[midpoint] < nums[left]:
                #lowest will be between 2nd point and midpoint
                right = midpoint
                left += 1
            #2: case where last point in an array is less than center
            else:
                #lowest will be between midpoint + 1 and end
                left = midpoint + 1
            midpoint = (left + right) / 2
        return nums[left]