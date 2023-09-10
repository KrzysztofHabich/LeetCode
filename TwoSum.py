from typing import List 

# Description: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a dictionary to store the values
        dict = {}
        #loop through the list
        for i in range(len(nums)):
            #check if the target - current number is in the dictionary
            if target - nums[i] in dict:
                #if it is, return the index of the current number and the index of the target - current number
                return [dict[target - nums[i]], i]
            #if it is not, add the current number and its index to the dictionary
            else:
                dict[nums[i]] = i
        #if no solution is found, return an empty list
        return []

#code to run when called from command-line
if __name__ == "__main__":
    solution = Solution()

    nums = [2,7,11,15]
    target = 9
    print(f"Given nums = {nums}, target = {target}, return {solution.twoSum(nums, target)}")

    nums = [3,2,4] 
    target = 6
    print(f"Given nums = {nums}, target = {target}, return {solution.twoSum(nums, target)}")

    nums = [3,3]
    target = 6
    print(f"Given nums = {nums}, target = {target}, return {solution.twoSum(nums, target)}")