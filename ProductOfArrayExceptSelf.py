'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for a in range(len(nums)):
            output.append(1)
        total = 1
        for a in range(len(nums) - 1):
            output[a + 1] = nums[a] * total
            total = output[a + 1]
        #now we have an array where nums[max] is correct because output[a] countains nums[1]*nums[2]...*nums[a-1]
        #now we loop in reverse to account for numbers after nums[a]
        a = len(nums) - 2
        total = 1
        while a >= 0:
            output[a] *= nums[a + 1] * total
            total = nums[a + 1] * total
            a -= 1
        return output