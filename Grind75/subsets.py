class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.dfs(nums, [], [])
    def dfs(self, nums, path, returnList):
        returnList.append(path)
        for a in range(len(nums)):
           self.combinations(nums[a + 1:], path + [nums[a]], returnList)
        return returnList