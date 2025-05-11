class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize a dictionary to count occurrences of each number
        ans_dict = {}

        # Iterate over each number in the list
        for num in nums:
            # If number is already in dictionary, increment its count
            if num in ans_dict:
                ans_dict[num] += 1
            # If it's not in the dictionary, initialize its count to 1
            else:
                ans_dict[num] = 1

        # The number with the minimum count (which will be 1) is the single number
        ans = min(ans_dict, key=ans_dict.get)

        return ans