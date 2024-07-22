#first attempt
#run time: 
#for num in nums: is O(n) where n is the length of values in given array nums
#for i in range(0,k): is O(k) where k is the size of given int k
#for key, value in mydict.items(): is O(l) where l is the length of values in dict size l
#total run time is O(k*l)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for num in nums:
            if num in mydict:
                mydict[num] += 1
            else:
                mydict[num] = 1
        print(mydict)
        result = []
        for i in range(0,k):
            curhighval = 0
            curhighkey = 0
            for key, value in mydict.items():
                print('iteration ',i)
                print("key:",key,"value:",value)
                print("curhighkey:",curhighkey,"curhighval:",curhighval)
                if value > curhighval:
                    print('passed')
                    curhighval = value
                    curhighkey = key
                    print("newcurhoghkey:",key,"newcurhighval:",value)


            result.append(key)
            del mydict[curhighkey]
        return result

#second attempt
#run time: O(n+1) + O(m) = O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        #O(n) where n is the length of values in given array nums
        for num in nums:
            if num in mydict:
                mydict[num] += 1
            else:
                mydict[num] = 1
        freq = []
        #O(n+1) 
        for i in range(0,len(nums)+1):
            freq.append([])
        #O(n) 
        for key, val in mydict.items():
            freq[val].append(key)
        result = []
        #O(n+1).
        for i in range(len(freq)-1,0, -1):
            if freq[i] != []:
                #O(m) where m is tha values in freq[i]
                for j in freq[i]:
                    result.append(j)
                    k = k - 1
                    if k == 0:
                        return result     
        return result
