class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = ""
        ret = 0
        #remove whitespace
        while len(s) > 0:
            if s[0] != " ":
                break
            s = s[1:]
        if s == "":
            return 0
        #sign check
        negative = False
        if s[0] == "-":
            negative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        for a in range(len(s)):
            if not (s[a] >= "0" and s[a] <= "9"):
                break
            out += s[a]
        if out == "":
            return 0
        if int(out) > (2**31 - 1):
            ret = 2**31 - 1
            if negative:
                ret += 1
                ret = -ret
        else:
            ret = int(out)
            if negative:
                ret = -ret
        return ret