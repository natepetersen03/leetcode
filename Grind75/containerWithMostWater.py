class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maximum = min([height[0], height[1]])
        a = 0
        b = len(height) - 1
        while (a < b):
            minHeight = min([height[a], height[b]])
            area = (b - a) * minHeight
            maximum = max([maximum, area])
            if (minHeight == height[a] and minHeight == height[b]):
                a += 1
                b -= 1
            elif minHeight == height[a]:
                while (height[a] <= minHeight):
                    a += 1
            else:
                while (height[b] <= minHeight):
                    b -= 1
        return maximum