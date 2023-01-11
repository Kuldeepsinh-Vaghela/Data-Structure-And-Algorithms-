#  Question 2 
#  leet code que 1: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#  You may assume that each input would have exactly one solution, and you may not use the same element twice.

#  You can return the answer in any order.

def twosum(nums,target):
    for num in nums:
            num_indx = nums.index(num)
            lookup_num = target - num
            #  checking if the lookup_num is in the list from the index after that of num
            if lookup_num in nums[nums.index(num)+1:]:
                #  finding the index of look_up number 
                #  if list = [3,2,3] ,target=6, num=3, lookup_num = 3, lookup_num_index = 1 using below line of code
                lookup_num_index = nums[nums.index(num)+1:].index(lookup_num)
                #  if list = [3,2,3] and target is 6, lookup_num = 3, lookup_num_index will be 1 using above code line 
                #  so adding the num_indx value and 1 to get accurate value of lookup_num_index 
                print( [num_indx, lookup_num_index+num_indx+1])
                break
twosum([3,2,3],6)
# ans = [0,2]
#  Time Complexity = O(n*2)
#  Space Complexity = O(1)
# Method 2
def two_sum(nums,target):
    for indx,num in enumerate(nums):
        lookup_num = target - num
        if lookup_num in nums[indx+1:]:
            lookup_num_index = nums[indx+1:].index(lookup_num)
            print([indx,lookup_num_index + indx + 1])
two_sum([3,2,3],6)


# Use Case:1 
# nums = [2,7,11,15]
# target = 9
# output = [0,1]

# Use Case:2
# nums = [3,2,4]
# target = 6
# output = [1,2]

# Use Case:3
# nums = [3,3]
# target = 6 
# output = [0,1]
  