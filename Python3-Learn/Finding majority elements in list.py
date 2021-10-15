#Leet code:-
#169. Majority Element
#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
 
#Example 1:
#Input: nums = [3,2,3]
#Output: 3
  
#Example 2:
#Input: nums = [2,2,1,1,1,2,2]
#Output: 2
  
#Constraints:
#•	n == nums.length
#•	1 <= n <= 5 * 104
#•	-231 <= nums[i] <= 231 – 1


#code:-
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        n = len(nums)/2
        for ele in nums:
            try:
                dict[ele] += 1
            except:
                dict[ele] = 1
        for item in dict:
            if dict[item] >= n:
                return item

#Explanation:-
#In this solution, simply count the numbers of same elements and check this condition ⌊n / 2⌋  if it is true then print(or return) the  item.
#In this I am taking a dictionary ( dict ={} ) to count the number of same elements occur in list (i.e., nums) then check the condition       
#n = len(nums)/2
#if dict[item] >= n:
#if it is true return item 

 
