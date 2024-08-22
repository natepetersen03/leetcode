'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # iterate through intervals, keeping an output array
        intervals.sort()
        outIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            currInter = intervals[i]
            # if the left of the current interval overlaps with the right of the previously combined interval
            if currInter[0] <= outIntervals[len(outIntervals) - 1][1]:
                currInter = [outIntervals[len(outIntervals) - 1][0], max([currInter[1], outIntervals[len(outIntervals) - 1][1]])]
                outIntervals = outIntervals[:len(outIntervals) - 1]
            outIntervals.append(currInter)
        return outIntervals