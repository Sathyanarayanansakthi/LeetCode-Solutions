"""Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        STEPS 
         1.no negative numbers
         2.while loop creation
         3.check it is palindrome or not
         4.return the number

        """
        # Remove all negative numbers 
        if x < 0:
            return False
        #Creating loop
        org=x
        a = 0
        while x > 0:
            dig = x % 10
            a = a * 10 + dig
            x //= 10
        return org == a
