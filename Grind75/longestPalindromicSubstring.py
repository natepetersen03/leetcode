class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #dp: base case 1. s[0] returns 1
        longestS = s[0]
        longest = 1

        # as a (len of substring of s) increases, we have left and right pointers. Since we've 
        # accounted for solutions from s[0:a], we only need to increment the left pointer
        # when a match is not found
        
        for a in range(1, len(s)):
            left = 0
            right = a
            #while there is a possibility of a greater palindrome
            leftP = left
            rightP = right
            while (left + longest <= right):
                #palindrome found of odd length
                if leftP == rightP:
                    if right - left + 1 > longest:
                        longestS = s[left:right + 1]
                        longest = right - left + 1
                    break
                if (leftP + 1 == rightP):
                    #palindrome found of even length
                    if (s[leftP] == s[rightP]):
                        if right - left + 1 > longest:
                            longestS = s[left:right + 1]
                            longest = right - left + 1
                        break  
                    #middle two characters not the same     
                    else:
                        left += 1
                        leftP = left
                        rightP = right
                        continue
                #palindrome possible
                if (s[leftP] == s[rightP]):
                    leftP += 1
                    rightP -= 1
                #palindrome impossible
                else:
                    left += 1
                    leftP = left
                    rightP = right
        return longestS