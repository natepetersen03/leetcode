'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        totalEntries = len(matrix) * len(matrix[0])
        visited = 0
        row = 0
        col = 0
        direction = "r"
        outArr = []
        while visited < totalEntries:
            outArr.append(matrix[row][col])
            visited += 1
            matrix[row][col] = None
            if direction == "r":
                if col < (len(matrix[row]) - 1):
                    col += 1
                else:
                    direction = "d"
                    row += 1
            elif direction == "l":
                if col > 0:
                    col -= 1
                else:
                    direction = "u"
                    row -= 1
            elif direction == "u":
                if row > 0:
                    row -= 1
                else:
                    direction = "r"
                    col += 1
            else:
                if row < (len(matrix) - 1):
                    row += 1
                else:
                    direction = "l"
                    col -= 1
            if visited == totalEntries:
                break
            if matrix[row][col] == None:
                if direction == "r":
                    col -= 1
                    row += 1
                    direction = "d"
                elif direction == "l":
                    col += 1
                    row -= 1
                    direction = "u"
                elif direction == "u":
                    row += 1
                    col += 1
                    direction = "r"
                else:
                    row -= 1
                    col -= 1
                    direction = "l"
        return outArr