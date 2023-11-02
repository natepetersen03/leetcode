class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for a in range(len(nums)):
            if (not (nums[a] in hmap.keys())):
                hmap[nums[a]] = [a]
            else:
                hmap[nums[a]].append(a)
        for a in range(len(nums)):
            if (target - nums[a] in hmap.keys()):
                if (target - nums[a] == nums[a]):
                    if (len(hmap[nums[a]]) > 1):
                        return hmap[nums[a]]
                else:
                    return[hmap[nums[a]][0], hmap[target - nums[a]][0]]
        return 'not found'