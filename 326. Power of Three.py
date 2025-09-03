"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1). """


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        If n is less than or equal to 0, return False
        Otherwise, keep dividing n by 3 while it is divisible
        If the final result is 1, then n is a power of 3 (return True)
        otherwise return False
        """

        if n <= 0:
            return False
        while n % 3 == 0:   
            n //= 3
        return n == 1
