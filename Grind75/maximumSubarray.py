'''
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dp -> base case is nums[0]
        maxSum = nums[0]
        currSum = nums[0]
        for a in range(1, len(nums)):
            # if the current sum is positive and adding the current number to the sum
            # doesn't make it negative
            if currSum > 0 and currSum + nums[a] >= 0:
                #add the current number to the total
                currSum += nums[a]
            else:
                #the sum is the current number
                currSum = nums[a]
            maxSum = max(currSum, maxSum)
        return maxSum