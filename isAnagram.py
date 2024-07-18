#first try, 5 mins
# this one checks for the same letters in the word, but it doesnt check to see if the same letters are used the same amount of times
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = set(s)
        tSet = set(t)
        if len(sSet) == len(tSet):
            for i in sSet:
                if i not in tSet:
                    return False
        return True
#second try, 6 mins
# this checks to see if the same letters are used the same amount of times

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        sSet = set(s)
        tSet = set(t)
        if len(sSet) != len(tSet):
            return False
            
        for i in s:
            if i in sdict:
                sdict[i] = sdict[i] + 1
            else:
                sdict[i] = 1
        for i in t:
            if i in tdict:
                tdict[i] = tdict[i] + 1
            else:
                tdict[i] = 1
        return sdict == tdict
#third try, is this better space complexity? there is only one dictionary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}     
        for i in s:
            if i in sdict:
                sdict[i] = sdict[i] + 1
            else:
                sdict[i] = 1
        for i in t:
            if i in sdict:
                sdict[i] = sdict[i] - 1
            else:
                return False
        for i in sdict:
            if sdict[i] > 0:
                return False

        return True
  #last try, for space complexity
  class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
