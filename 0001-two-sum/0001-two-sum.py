class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) > 2:
            sort_nums = sorted(nums)
            a = 0
            b = len(nums)-1
            while a<b:
                if sort_nums[a]+sort_nums[b] == target:
                    indx_1 = nums.index(sort_nums[a])
                    nums[indx_1] = -9999
                    indx_2 = nums.index(sort_nums[b])
                    return [indx_1, indx_2]
                elif sort_nums[a]+sort_nums[b] > target:
                    b -= 1
                else: 
                    a += 1
            return [nums.index(sort_nums[a]),nums.index(sort_nums[b])]
        elif len(nums) == 1 :
            return [0]
        else:
            return [0,1]
        