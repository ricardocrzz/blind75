#first solution
#making empty dictionary (a dictionary cant have duplicate values)
#iterate through nums array
#for every iteration, see if the current number in array is in duplicate
#if so, return true because its already there, therefore there is a dupe
#if not, add it to the dictionary and continue
#once array for loop is done, return False because there was no dupe
#time complexity:
#O(n) for loop
#O(1) for in numsDict
#O(1) for numsDict[i] = 1
#total, O(n)
#space complexity is the new dict, O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}
        for i in nums:
            if i in numsDict:
                return True
            else:
                numsDict[i] = 1 
        return False
#second solution
#same thing basically, mySet = set(nums) is O(n)
#space complexity is the new set, O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)
        if len(mySet) == len(nums):
            return False
        else: 
            return True
