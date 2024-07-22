class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for i in s:
            if (ord(i) >= ord('A') and ord(i) <= ord('z')) or (ord(i) >= ord('0') and ord(i) <= ord('9')):
                newString += i
        s = newString.lower()
        if len(s) == 0:
            return True
        if len(s) == 1:
            return True
        s1 = ""
        s2 = ""
        print(len(s))
        print(math.floor(len(s)/2))
        for i in range(0, math.floor(len(s)/2)):
            print(i)
            s1 += s[i]
        for i in range(len(s)-1, math.floor(len(s)/2)-1, -1):
            s2 += s[i]
        print(s1+s2)
        if (len(s1) - len(s2) != 0):
            s2 = s2[:-1]
        if s1 == s2:
            return True
        return False


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<=right:
            while left<right and ((ord(s[left]) >= ord('A') and ord(s[left]) <= ord('z')) == False and (ord(s[left]) >= ord('0') and ord(s[left]) <= ord('9')) == False):
                left += 1
            while left<right and ((ord(s[right]) >= ord('A') and ord(s[right]) <= ord('z')) == False and (ord(s[right]) >= ord('0') and ord(s[right]) <= ord('9')) == False):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True