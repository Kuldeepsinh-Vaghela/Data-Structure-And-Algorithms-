#  Question 1
#  Find the missing number in an integer array of 1 to 100
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,\
    19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, \
        37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,\
             55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, \
                74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,\
                     91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def missing_value(list_of_integers,n):
    nmbr = 1
    while nmbr <= n:
        if nmbr not in list_of_integers:
            print("The missing number is:", nmbr)
            nmbr += 1
        else:
            nmbr += 1
missing_value(mylist,100)

#  Time Complexity = O(n*2)
#  Space Complexity = O(1)

#  Other method
def msng_value(list_of_int,n):
    sum_of_n_int = (n*(n+1))/2
    sum_of_int_in_list = sum(list_of_int)
    print("The missing value using method 2 is:", sum_of_n_int-sum_of_int_in_list)
msng_value(mylist,100)

#  Time Complexity = O(n)
#  Space Complexity = O(1)

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
#  Time Complexity = O(n*3)
#  Space Complexity = O(1)

def two_sum(nums,target):
    for indx,num in enumerate(nums):
        lookup_num = target - num
        if lookup_num in nums[indx+1:]:
            lookup_num_index = nums[indx+1:].index(lookup_num)
            print([indx,lookup_num_index + indx + 1])
two_sum([3,2,3],6)

#  Question 3
#  leet code array 26: Remove Duplicates from Sorted Array
def removeDuplicates(nums):
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                i+= 1
                nums[i] = nums[j]   
        #return i+1
        print(nums)
removeDuplicates([0,0,1,1,1,1,2,2,3,3,3,4,4])

#  Question 4
#  Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

def removeElement(nums, val):
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j  += 1
        #return j
        print(nums)
removeElement([0,0,1,1,1,1,2,2,3,3,3,4,4], 3)