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
        #base cases
        left = 0
        right = len(nums) - 1
        midpoint = (left + right) / 2
        if (len(nums) == 2):
            if nums[0] == target:
                return 0 
            if nums[1] == target:
                return 1
        if (len(nums) == 1):
            if nums[0] == target:
                return 0
        #loop while left + 1 <= right
        while left + 1 <= right:
            if nums[left] < nums[midpoint]:
                #target is inbetween
                if target <= nums[midpoint] and target >= nums[left]:
                    right = midpoint
                else:
                    left = midpoint
            else:
                #target is inbetween midpoint and right
                if target >= nums[midpoint] and target <= nums[right]:
                    left = midpoint
                else:
                    right = midpoint
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            left += 1
            right -= 1
            midpoint = (left + right) / 2
        if nums[midpoint] == target:
            return midpoint
        return -1  