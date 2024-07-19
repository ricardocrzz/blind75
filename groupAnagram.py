#first try whooped my butt, tried to make a dictionary and compare all values.
#python wouldnt let me make a dictrionary of dictionaries

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listdict = []
        counter = 0
        for word in strs: #ACT, POTS
            currentdict = {}
            for letter in word: # A, C, T then P,O,T,S
                if letter in currentdict: 
                    currentdict[letter] += 1
                else: 
                    currentdict[letter] = 1
            #{a:1,c:1,t:1}
            listdict.append(currentdict)
            #[{a:1,c:1,t:1}]
            counter = counter +1
        #listdict = [{a:1,c:1,t:1},{p:1,o:1,t:1,s:1},{p:1,o:1,t:1,s:1},{a:1,c:1,t:1},{p:1,o:1,t:1,s:1},{a:1,h:1,t:1}]
        for i in range(0, len(listdict)):
            for j in range(i+1, len(listdict)):
                if listdict[i] == listdict[j]:
                    print(strs[i], strs[j])
                    print(True)
                    print(i,j, listdict[i], "||||||", listdict[j])


        return [[""]]

        finaldict = {}
        for wordbrokendown in listdict: #[{a:1,c:1,t:1},{p:1,o:1,t:1,s:1},...]
            #{a:1,c:1,t:1}
            if wordbrokendown in finaldict:
                finaldict[wordbrokendown]  = finaldict[wordbrokendown] + 1
            else:
                finaldict[wordbrokendown]  = 1
        #{ {a:1,c:1,t:1}:2 , {p:1,o:1,t:1,s:1}:3,...}
        print(finaldict)
        return [[""]]
         counter2 = 0
        for word in strs: #ACT, POTS
            for letter in word: # A, C, T then P,O,T,S
                if letter in currentdict: 
                    currentdict[letter] = currentdict[letter] + 1
                else: 
                    currentdict[letter] = 1
            if currentdict in finaldict: #if {a:1,c:1,t:1} in 
                result[]

#second try, i sorted each word in the strs array, 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedwords = []
        for word in strs:
            wordinchars = sorted(word)
            newword = ""
            for char in wordinchars:
                newword += char
            sortedwords.append(newword)
        print(sortedwords)
        setofwords = set(sortedwords)
        print(setofwords)
        listofsetofwords = list(setofwords)
        print(listofsetofwords)
        dictofwords = {}
        for i in range(0,len(strs)):
            dictofwords[strs[i]] = sortedwords[i]
        print(dictofwords)
        anagrams = []
        for i in range(0,len(setofwords)):
            anagrams.append([])
        print(anagrams)
        for word in strs:
            print(word,dictofwords[word])
            if dictofwords[word] in setofwords:
                print(listofsetofwords.index(dictofwords[word]))
                #anagrams[setofword]
                anagrams[listofsetofwords.index(dictofwords[word])].append(word)
        return anagrams
