class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        highest_streak = 0
        for num in set_nums:
            if (num -1) not in set_nums:
                curr_streak = 1
                curr_num = num
                while (curr_num + 1) in set_nums:
                    curr_streak += 1
                    curr_num += 1
                highest_streak = max(highest_streak,curr_streak)
        return highest_streak

        