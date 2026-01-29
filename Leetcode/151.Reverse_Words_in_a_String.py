
class Solution:
    def reverseWords(self, s: str) -> str:
        print(s)
        a = s.split()
        print(a)
        b = []
        for i in a:
            b.insert(0,i)
        print(b)
        c = " ".join(b)
        print(c)
        return c


p1 = Solution()
p1.reverseWords("the sky is blue")