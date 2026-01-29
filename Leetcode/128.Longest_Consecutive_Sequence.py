class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        num2 = sorted(nums)
        print(num2)
        setout = sorted(set(num2))
        print(setout)
        outlist = list(setout)
        out = 0
        j = 1
        maax = 1 
        longest = 1
        for i in range(len(outlist)):
            #print(outlist[i])
            if j == len(setout):
                break
            if outlist[i] - outlist[j] == -1:
                print(outlist[i])
                print(outlist[j])
                maax += 1
                j += 1
                print(maax)
                print('------')
            else:
                longest = max(longest, maax)
                maax = 1
                j += 1
        print(longest)
        return max(longest, maax)

p1 = Solution()
print(p1.longestConsecutive([1,2,6,7,8]))
