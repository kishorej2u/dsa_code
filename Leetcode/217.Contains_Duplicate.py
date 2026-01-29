
class solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # print(nums)
        # temp_nums = []
        # for i in nums:
        #     if i not in temp_nums:
        #         temp_nums.append(i)
        #     else:
        #         return True
        
        # if len(temp_nums) == len(nums):
        #     print(temp_nums)
        #     return False
        print(nums)
        setout = set(nums)
        if len(setout) == len(nums):
            return False
        else:
            return True


s1 = solution()
print(s1.containsDuplicate([1, 2, 3, 4, 1]))
