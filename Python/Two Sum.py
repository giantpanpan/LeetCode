"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]

"""

#O(n^2)

class Solution:
    def twoSum(self, nums, target):
        dictionary ={}
        for i in range(len(nums)):
            dictionary[i] = nums[i]             #create a dictionary for this list

        i =0
        while i < len(nums):
            value = target-dictionary[i]        #get the value need 
            for k,v in dictionary.items():      #look up for key with this value and the key is not the current index
                if value == v and i != k:
                    return [i,k]
            i+=1
                    
            

#O(n)
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):            #store the required number as key and the index of current number as value in a dictionary
            if nums[i] in buff_dict:          #if current number equals to any key in the dictionary,
                                              #return the current index and the value(index of the paired number in dictionary)
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
            print (buff_dict)
        
a = Solution()
print(a.twoSum([2, 7, 11, 15],18))
