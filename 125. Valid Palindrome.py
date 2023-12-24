class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=''
        for i in s:
            if i.isalnum():
            #if i.isalpha() or i.isdigit():
                i=i.lower()
                str1+=i
        print(str1)
        if str1==str1[::-1]:
            return True
        else: return False
