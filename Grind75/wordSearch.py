'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        maxM, maxN = len(board), len(board[0])
        for a in range(len(board)):
            for b in range(len(board[a])):
                if board[a][b] == word[0]:
                    if self.dfs(board, a, b, word, 0, maxM, maxN):
                        return True
        return False
    def dfs(self, board, m, n, word, pos, maxM, maxN):
        if m < 0 or n < 0 or m == maxM or n == maxN:
            return False
        if board[m][n] != word[pos]:
            return False
        if pos == len(word) - 1 and word[pos] == board[m][n]:
            return True
        board[m][n] = '#'
        if self.dfs(board, m + 1, n, word, pos + 1, maxM, maxN) or self.dfs(board, m - 1, n, word, pos + 1, maxM, maxN) or self.dfs(board, m, n + 1, word, pos + 1, maxM, maxN) or self.dfs(board, m, n - 1, word, pos + 1, maxM, maxN):
            return True
        board[m][n] = word[pos]
        return False