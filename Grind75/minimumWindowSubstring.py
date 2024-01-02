'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #COME BACK TO THIS
        tSet = Counter(t)
        tLen = len(tSet.keys())
        sSet = Counter()
        left, right = 0, -1
        match = 0
        res = ""
        if len(t) > len(s) or len(s) == 0:
            return ""
        while right < len(s):
            # options : 1. extend (aka increment right pointer)
            if match < tLen:
                if right == len(s) - 1:
                    return res
                right += 1
                sSet[s[right]] += 1
                if sSet[s[right]] == tSet[s[right]]:
                    match += 1
            # 2. contract
            else:
                sSet[s[left]] -= 1
                if sSet[s[left]] < tSet[s[left]] and tSet[s[left]] > 0:
                    match -= 1
                left += 1
            # check for smaller window given that current substring is valid window
            if match == tLen and (len(s[left:right + 1]) < len(res) or res == ""):
                res = s[left:right + 1]
        return res