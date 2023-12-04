class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        '''
        Steps:
        for each digit, branch out with different possibilities and rest of string
        Helper function. Base case: string = "", otherwise return with list of all possibilities
        so far and remove first character from string.
        '''
        def digitHelper(self, digits, combinations, d):
            if digits == "":
                return combinations
            if len(combinations) == 0:
                for element in d[digits[0]]:
                    combinations.append(element)
            else:
                comboLength = len(combinations)
                for a in range(comboLength - 1, -1, -1):
                    curr = combinations.pop(a)
                    for element in d[digits[0]]:
                        combinations.append(curr + element)
            return digitHelper(self, digits[1:], combinations, d)
        d = {"2" : ["a", "b", "c"], "3" : ["d", "e", "f"], "4" : ["g", "h", "i"],
        "5" : ["j", "k", "l"], "6" : ["m", "n", "o"], "7" : ["p", "q", "r", "s"],
        "8": ["t", "u", "v"], "9" : ["w", "x", "y", "z"]}
        return digitHelper(self, digits, [], d)