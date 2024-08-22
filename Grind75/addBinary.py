'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        outStr = ""
        while a != "" or b != "":
            if a == "":
                a += "0"
            if b == "":
                b += "0"
            sumInt = int(a[-1]) + int(b[-1]) + carry
            if sumInt == 3:
                outStr = "1" + outStr
            elif sumInt == 2:
                outStr = "0" + outStr
                carry = 1
            elif sumInt == 1:
                outStr = "1" + outStr
                carry = 0
            else:
                outStr = "0" + outStr
            a = a[:-1]
            b = b[:-1]
        if carry == 1:
            outStr = "1" + outStr
        return outStr