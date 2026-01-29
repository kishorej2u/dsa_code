

class Solution:
    def checkpalindrome(self, temp):
        if temp == temp[::-1]:
            return True
        else:
            return False 
    def longestPalindrome(self, s: str) -> str:
        #print(s)
        r = len(s)
        
        for i in range(len(s)):
            #print(s[i:r])
            temp = s[i:r]
            if self.checkpalindrome(temp) == True:
                print(temp)
            else:
                r -= 1
        



p1 = Solution()
p1.longestPalindrome("babad")