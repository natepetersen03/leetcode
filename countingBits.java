/*
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

 */

class Solution {
    public int[] countBits(int n) {
        int[] returnSize = new int[n + 1];
        returnSize[0] = 0;
        for (int a = 1; a <= n; a++) {
            if (a % 2 != 0) {
                returnSize[a] = returnSize[a - 1] + 1;
            } else {
                int b = a;
                while (b % 2 == 0) {
                    b = b / 2;
                }
                returnSize[a] = returnSize[b];
            }
        }
        return returnSize;
    }
}