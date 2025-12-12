class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_freq = {}
        len_nums = len(nums)
        for num in nums:
            num_freq[num] = num_freq.get(num,0) + 1
            if num_freq[num] > len_nums/2:
                return num
        # for key,value in num_freq.items():
        #     if value > len(nums)/2:
        #         return key
