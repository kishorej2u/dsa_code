

class Solution:

    def longestPalindrome(self, s: str) -> str:
        maxi = ''
        max_len = 0
        for i in range (len(s)):
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    maxi = (s[l:r+1])
                    print(maxi)
                    max_len = (r - l +1)
                l -=1
                r +=1 
            print(maxi)
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    maxi = (s[l:r+1])
                    print(maxi)
                    max_len = (r - l +1)
                l -=1
                r +=1 
            print(maxi)
        return maxi




p1 = Solution()
p1.longestPalindrome("baad")





# class Solution:
#     def checkpalindrome(self, temp):
#         if temp == temp[::-1]:
#             return True
#         else:
#             return False 
#     def longestPalindrome(self, s: str) -> str:
#         maxi = ''
#         for i in range(len(s)):
#             for k in range(1,len(s)+1):
#                 temp = s[i:i+k]
#                 #print(temp)
#                 if self.checkpalindrome(temp) == True:
#                     if len(temp) > len(maxi):
#                         maxi = temp

#         print(maxi)
#         return maxi