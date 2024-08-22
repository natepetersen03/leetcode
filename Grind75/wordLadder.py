'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
'''

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #preprocessing and mapping all words with one letter removed in dictionary to the actual word
        d = {}
        for word in wordList:
            for a in range(len(word)):
                currString = word[:a] + '_' + word[a+1:]
                d[currString] = d.get(currString, []) + [word]
        queue = [(beginWord, 1)]
        currWord = beginWord
        s = set()
        #bfs
        while queue:
            currWord, depth = queue.pop(0)
            s.add(currWord)
            if currWord == endWord:
                return depth
            for a in range(len(currWord)):
                currString = currWord[:a] + '_' + currWord[a+1:]
                neighbors = d.get(currString, [])
                for neighbor in neighbors:
                    if not (neighbor in s):
                        queue.append((neighbor, depth + 1))             
        return 0