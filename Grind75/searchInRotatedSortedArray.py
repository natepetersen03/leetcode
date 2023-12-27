'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #logic: check which half is sorted. 
        #if inside sorted segment, search through that, else search through other
        left = 0
        right = len(nums) - 1
        while left < right:
            midpoint = (left + right) / 2
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[midpoint] == target:
                return midpoint
            #left side is sorted
            if nums[left] < nums[midpoint]:
                #between left and midpoint
                if target > nums[left] and target < nums[midpoint]:
                    right = midpoint - 1
                else:
                    left = midpoint + 1
            #right side is sorted
            else:
                #between midpoint and right
                if target > nums[midpoint] and target < nums[right]:
                    left = midpoint + 1
                else:
                    right = midpoint - 1
        return left if nums[left] == target else -1
