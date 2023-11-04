'''
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #initialize base cases
        minimum = nums[0]
        maximum = nums[0]
        answer = nums[0]
        #iterate
        for a in range(1, len(nums)):
            tempMin = minimum
            #two pointers, min and max. Based on current number and previous maximal/minimal product in subarray.
            minimum = min([nums[a], minimum * nums[a], maximum * nums[a]])
            maximum = max([nums[a], tempMin * nums[a], maximum * nums[a]])
            #update answer
            answer = max([answer, maximum])
        return answer