'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        outlist = []
        for a in range(len(nums) - 2):
            #if nums[a] = nums[a - 1]
            if (a != 0 and nums[a] == nums[a - 1]):
                continue
            #initialize high and low pointe htat are both above a
            high = len(nums) - 1
            low = a + 1
            while (low < high):
                #sum = 0
                if (nums[high] + nums[low] + nums[a]) == 0:
                    outlist.append([nums[a], nums[low], nums[high]])
                    #accounting for duplicates
                    while (nums[high - 1] == nums[high] and high > low):
                        high -= 1
                    while (nums[low] == nums[low + 1] and low < high):
                        low += 1
                    high -= 1
                    low += 1
                # sum < 0
                elif (nums[high] + nums[low] + nums[a]) < 0:
                    low += 1
                # sum > 0
                else:
                    high -= 1
        return outlist