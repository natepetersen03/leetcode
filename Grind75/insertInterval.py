'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # COME BACK TO THIS PROBLEM BC THIS SOLUTION IS INSANE
        left, right = newInterval[0], newInterval[1]
        returnIntervals = []
        addedInt = []
        if len(intervals) == 0:
            returnIntervals.append(newInterval)
            return returnIntervals
        if right < intervals[0][0]:
            return [newInterval] + intervals
        if left > intervals[len(intervals) - 1][1]:
            return intervals + [newInterval]
        # go through and find where the left bound will go:
        for inter in range(len(intervals)):
            currL, currR = intervals[inter][0], intervals[inter][1]
            if len(addedInt) == 0:
                # cases: left bound is already inside of an interval -> don't edit left bound of existing intervals
                if currL <= left and currR >= left:
                    addedInt.append(currL)
                # left bound is not inside of an interval -> left bound of next existing interval = given left bound
                elif left <= currL:
                    if inter == 0:
                        addedInt.append(left)
                    #previous right interval is less than given left
                    elif intervals[inter - 1][1] < left:
                        if currL > right:
                            returnIntervals.append(newInterval)
                            addedInt.append(currL)
                        else:
                            addedInt.append(left)
            # once left bound is found, search for right bound.
            if len(addedInt) == 1:
                # if right bound is inside of existing interval use right bound of that one, but combine all intervals up to then
                if currL <= right and currR >= right:
                    addedInt.append(currR)
                # if it is not inside of existing interval, right bound of existing interval = given right bound
                elif right >= currR:
                    if inter + 1 == len(intervals):
                        addedInt.append(right)
                    # if next left is less than given right
                    elif intervals[inter + 1][0] > right:
                        addedInt.append(right)
                # case where new interval was sandwiched between two intervals, add currR
                elif returnIntervals[-1] == newInterval:
                    addedInt.append(currR)
            #our current interval range doesn't correspond with the targetInterval
            if len(addedInt) == 0:
                addedInt.append(currL)
                addedInt.append(currR)
            #we have a new interval that we can add to the output
            if len(addedInt) == 2:
                returnIntervals.append(list(tuple(addedInt)))
                addedInt = []
        return returnIntervals