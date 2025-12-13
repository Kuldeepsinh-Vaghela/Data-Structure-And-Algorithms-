class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        map_dic = {}
        for num in nums:
            map_dic[num] = 1
        for i in range(len(nums) + 1):
            if i not in map_dic:
                return i


        