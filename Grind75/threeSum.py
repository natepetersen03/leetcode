class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        Steps:
        1: sort list
        2: set one value in place and create left/right pointers
        3: if the sum > 0, right--, if sum < 0, left++
        4: if sum == 0, we add it to the result and left++/right--
        '''
        nums.sort()
        outList = []
        for a in range(1, len(nums) - 1):
            left = 0
            right = len(nums) - 1
            while left < a and right > a:
                currSum = nums[left] + nums[a] + nums[right]
                if currSum < 0:
                    left += 1
                if currSum > 0:
                    right -= 1
                if currSum == 0:
                    if not [nums[left], nums[a], nums[right]] in outList:
                        outList.append([nums[left], nums[a], nums[right]])
                    left += 1
                    right -= 1              
        return outList