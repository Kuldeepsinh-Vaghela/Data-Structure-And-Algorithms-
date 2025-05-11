#LeetCode Question (217): Contains Duplicate
#Given an integer array nums, return true if any value appears at least twice in the array,
#and return false if every element is distinct.
def containsDuplicate(nums):
        sorted_nums = sorted(nums)
        i = 0
        j = 1
        while j <= len(sorted_nums)-1:
            if sorted_nums[i] == sorted_nums[j]:
                 return True
            else:
                j+= 1
                i+= 1
        return False


