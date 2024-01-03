'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroes = []
        #grab indecies of all zeroes
        for ind in range(len(nums)):
            if nums[ind] == 0:
                zeroes.append(ind)
        #merge and swap in place while doing so
        index = 0
        #swap in place for all nums[0...len(zeroes) - 1].
        while len(zeroes) != 0:
            temp = nums[index]
            nums[index] = 0
            nums[zeroes[0]] = temp
            zeroes = zeroes[1:]
            index += 1
        #now zeroes are in order
        ones = []
        for ind in range(index, len(nums)):
            if nums[ind] == 1:
                ones.append(ind)
        while len(ones) != 0:
            temp = nums[index]
            nums[index] = 1
            nums[ones[0]] = temp
            ones = ones[1:]
            index += 1
        #now all in order
        return nums