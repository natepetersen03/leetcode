class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #back with set and queue. Set contains prev characters
        #in substring, queue = substring.
        queue = []
        se = set()
        longest = 0
        currL = 0
        for a in range(len(s)):
            queue.append(s[a])
            # check if the character is in the set
            if s[a] in se:
                for b in range(a):
                    curr = queue.pop(0)
                    se.remove(curr)
                    if curr == s[a]:
                        se.add(curr)
                        break
            else:
                se.add(s[a])
            currL = len(queue)
            longest = max([currL, longest])
        return longest