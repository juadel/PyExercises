# Given an Array of Integers, return indices of the numbers such
# that they add up to a specific target.
# You may assume that each input would have exactly 
# one solution, and you may not use the same element twice
from typing import List


class Solution:
    def __init__(self ):
        self.solution: List[int]

    def twoSum(self, nums: List[int] , target: int)-> List[int]:
        
        for i in range(len(nums)):
           for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            else:
                j=+1
    def twoSumEnum(self,nums: List[int] , target: int)-> List[int]:

        for index1, num1 in enumerate(nums):
            for index2 , num2 in enumerate(nums):
                if num1+num2 == target and index1!=index2:
                    return [index1,index2]
                    
           

sol = Solution()
array: List[int]=[2,7,11,15]
target:int = 9
sol.solution = sol.twoSumEnum(array,target)
print(sol.solution)

