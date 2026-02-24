

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out =set()
        l = r = 0
        max_len = 0
        while r < len(s):
            if s[r] not in out:
                out.add(s[r])
                #max_len = r -l + 1
                max_len = max(max_len, r - l + 1)
                r += 1
                print(out)
                print(max_len)
            else:
                while s[r] in out:
                    out.remove(s[l])
                    print(f'this is l {l}')
                    print(len(out))
                    l += 1
                    print(f'this is else {out}')
        print(max_len)
        return max_len
    
p1 = Solution()
p1.lengthOfLongestSubstring("abcabcbb")

