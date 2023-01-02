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
#  leet code 27: Given an integer array nums and an integer val, \
#  remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

def removeElement(nums, val):
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j  += 1
        #return j
        print(nums)
removeElement([0,0,1,1,1,1,2,2,3,3,3,4,4], 3)

#  Question 5
#  leet code 35: Search Insert Position
#  Given a sorted array of distinct integers and a target value, return the index if the target is found.\
#  If not, return the index where it would be if it were inserted in order.
#  You must write an algorithm with O(log n) runtime complexity
def searchInsert( nums, target):
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end  = mid - 1
            if nums[mid] < target:
                start = mid + 1
        print( start)
searchInsert([1,3,5,6,7,8,9,10],4)

#  Question 6
#  leet code 66: You are given a large integer represented as an integer array digits, \
#  where each digits[i] is the ith digit of the integer. \
#  The digits are ordered from most significant to least significant in left-to-right order. \
#  The large integer does not contain any leading 0's.
#  Increment the large integer by one and return the resulting array of digits.
def plusOne(digits):
        n = 1
        if digits[-1] in [0,1,2,3,4,5,6,7,8]:
            digits[-1] += 1
            return digits
        else:
            while n <= len(digits):
                if digits[-n] == 9:
                    if len(digits) ==1:
                        digits[-1] = 0
                        digits.insert(0,1)
                        return digits
                    else:
                        digits[-n] = 0
                        n += 1
                else:
                    digits[-n] += 1
                    break
            if digits[0] == 0:
                digits.insert(0,1)   
            return digits
a = plusOne([9,8,9])
print(a)

#  Question 7:
#  leet code 88: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,\
#  and two integers m and n, representing the number of elements in nums1 and nums2 respectively
#  Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#  The final sorted array should not be returned by the function, but instead be stored inside \
#  the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements \
#  denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.\
#  nums2 has a length of n.
def merge(nums1, m, nums2, n):
        nums1[m:] = nums2[0:]
        nums1.sort()

        return nums1
a = merge([1,2,3,0,0,0],3,[2,5,6],3)
print(a)

#  Question 8
#  Leet code 118: Pascals Triangle
#  Given an integer numRows, return the first numRows of Pascal's triangle.
def generate(numRows):
        i = [1,1]
        li = []
        if numRows == 1:
            li.append([1])
            return li
        elif numRows == 2:
            li.append([1])
            li.append(i)
            return li
        else:
            li.append([1])
            li.append(i)
            numRows -= 2
            while numRows > 0:
                j=[1]
                indx = 0
                while indx < len(i)-1:
                    a = i[indx]+ i[indx+1]
                    j.append(a)
                    indx += 1
                j.append(1)
                i = j
                numRows -= 1
                li.append(j)
        return li
a = generate(5)
print(a)


#  Question 9
#  leet code 119: Pascal's Triangle II
#  Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

def getRow(rowIndex):
        i = [1,1]
        li = []
        if rowIndex == 0:
            li.append([1])
            return li[rowIndex]
        elif rowIndex == 1:
            li.append([1])
            li.append(i)
            return li[rowIndex]
        else:
            li.append([1])
            li.append(i)
            new_rowIndex = rowIndex
            new_rowIndex -= 1
            while new_rowIndex > 0:
                j=[1]
                indx = 0
                while indx < len(i)-1:
                    a = i[indx]+ i[indx+1]
                    j.append(a)
                    indx += 1
                j.append(1)
                i = j
                new_rowIndex -= 1
                li.append(j)
        return li[rowIndex]
a = getRow(3)
print(a)

#  Question 10
#  leet code 121: Best Time to Buy and Sell Stock
#  You are given an array prices where prices[i] is the price of a given stock on the ith day
#  You want to maximize your profit by choosing a single day to buy one stock and choosing a \
#  different day in the future to sell that stock.
#  Return the maximum profit you can achieve from this transaction. If you cannot achieve any \
#  profit, return 0.

def maxProfit(prices):
        min_value_indx = 0
        max_value_indx = 1
        profit1 = []
        while max_value_indx <= len(prices)-1:
            min_value = prices[min_value_indx]
            max_value = prices[max_value_indx]
            if min_value > max_value:
                min_value_indx += 1
                max_value_indx = min_value_indx+ 1
            elif min_value == max_value:
                min_value_indx += 1
                max_value_indx = min_value_indx+1
            else:
                profit2 = max_value-min_value
                profit1.append(profit2)
                max_value_indx += 1
        if profit1 == []:
            return 0
        else:
            return max(profit1)
b = maxProfit([0,1,2,2,3,0,4,2])
print(b)