"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
""" 

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        """
        2arrays are there and need to compare the arrays and need to return the simlar values
         create 2 for loops and after that compare the u arrays and retun the simlar values in the array in an single array

         OR 
         create a sinlge loop in and compare bothe the values the return the values

        """
        result = []
        for x in nums1:
            for y in nums2:
                if x == y and x not in result:
                    result.append(x)
        return result
