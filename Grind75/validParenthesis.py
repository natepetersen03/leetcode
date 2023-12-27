class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        straightforward idea. Closed/opening works like stack, must be closed/
        opened in lifo order
        '''
        stack = []
        for a in range(len(s)):
            if s[a] in "{[(":
                stack.append(s[a])
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if s[a] == ")" and curr != "(":
                    return False
                if s[a] == "}" and curr != "{":
                    return False
                if s[a] == "]" and curr != "[":
                    return False
        return True if len(stack) == 0 else False