# Array Questions
## Question: 1
Find the missing number in an integer array of 1 to 100


```
Method 1
#Define missing_value(list_of_integers,n)
    #Initialize 'nmbr' variable to 1
    #While 'nmbr' is less then the number 'n' 
        #check if the value of the variable 'nmbr' is present in the 'list_of_integers'
        #if no
            #print out the value of the variable 'nmbr'
            #increase the value of 'nmbr' variable by 1
        #if yes
            #increase the value of 'nmbr' variable by 1
```

```
Method 2
#Define msng_value(list_of_int,n)
    #Initialize 'sum_of_n_int' variable to the formula for sum of n natural numbers
    #Initialize 'sum_of_int_in_list' variable to the sum of the elements in the 'list_of_int'
    #Subtract the value of 'sum_of_int_in_list' variable from 'sum_of_n_int' variable and print it out 

```

## Question: 2
### Leetcode Que 1: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

```

#Define twosum(nums,target)
    #for a value 'num' in the list 'nums'
        #find the index value of the 'num' and assign it to 'num_indx' variable
        #subtract 'num' from the 'target' and assign that value to 'lookup_num' variable
        #slice all the elements before 'num' and 'num' itself from the list 'nums' and check if the 'lookup_num' variable value is present in the list 'nums' with remaining variables
        #if yes
            #find the index of the 'lookup_num' variable value in the list 'nums' where all the elements before 'num' and 'num' itself are sliced and assign it to 'lookup_num_index' variable
            #add 'num_indx', 'lookup_num_index' and 1 to get the real index of the 'lookup_num' variable value in list 'nums' 
            #print out 'num_indx' variable and the real index of the 'lookup_num' variable value in list 'nums' 
            #break the loop

```

## Question: 3
### Leetcode Que 26: Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

```

#Define removeDuplicates(nums)
    #Initialize 'i' variable to 0
    #for variable 'j' in the range from 1 to length of list 'nums'
        #check if the value in list 'nums' at index 'j' and 'j'-1 is the same
        #if not
            #increase the value of 'i' by 1
            #reassign the value at 'i' index in list 'nums' to the value at 'j' index
    #print out the updated list 'nums'

```

## Question: 4
### Leetcode 27: Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

```

# Define removeElement(nums, val)
    #Initialize a variable 'j' to 0
    #for a variable 'i' in range 1 to the length of list 'nums'
        #check if the value in list 'nums' at index 'i' is same as 'val'
        #if not
            #reassign the value in list at index 'j' to the value at index 'i'
            #increase the value of 'j' by 1
    #print out the list 'nums'

```

## Question: 5
### Leetcode 35: Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

```

#Define searchInsert(nums, target)
    #Initialize a variable 'start' to 0
    #set the variable 'end' to the index value of the last element of list 'nums'
    #while 'start' is less than or equal to 'end'
        #set the variable 'mid' to the quotient value obtained after dividing sum of 'start' and 'end' by 2
        #check if the value in list 'nums' at index 'mid' is equal to 'target'
        #if yes
            #return mid
        #else check if the value in list 'nums' at index 'mid' is greater than 'target'
        #if yes
            #reassign the value of 'end' to 'mid'-1
        #check if the value in list 'nums' at index 'mid' is less than to 'target'
        #if yes
            #reassign the value of 'start' to 'mid'+1
    #print out the value of 'start' variable

``` 
## Question: 6
### Leetcode 66: Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
```

#Define plusOne(digits)
    #Initialize a variable 'n' to 1
    #check if the last element of list 'digits' is between numbers 1-8
    #if yes
        #increase the value of last element list 'digits' by 1
        #return the list 'digits'
    #if no
        #while variable 'n' is less than or equal to the length of the list 'digits'
            #check if the 'n'th value from the last of list 'digits' is 9
            #if yes
                #check if the length of list 'digits' is 1
                #if yes
                    #reassign the last value of list 'digits' to 0
                    #insert value '1' at the begining of the list 'digits'
                    #return the list 'digits'
                #if no
                    #reassign the value of the 'n'th element from the last of list 'digits' to 0
                    #increase the value of 'n' variable by 1
            #if no
                #increase the value of the 'n'th element from the last of list 'digits' by 1
                #break the loop
        #check if the first element of the list 'digits' is zero
        #if yes
            #insert a value '1' at the begining of list 'digits'
        #return the list 'digits'

```

## Question: 7
### Leetcode 88: Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

```

#Define merge(nums1, m, nums2, n)
    #reassign the last m elements of list 'nums1' to first 'n' elements of list 'nums2'
    #sort the elements in list 'nums1'
    #return the list 'nums1'

```

## Question: 8
### Leetcode 118: Pascals Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it

```

#Define generate(numRows)
    #set variable 'i' to list [1,1]
    #Initialize a variable 'li' as empty list
    #check if 'numRows' is equal to 1 
    #if yes
        #append a value '[1]' to the empty list 'li'
        #return list 'li'
    #else check if 'numRows' is equal to 2
    #if yes
        #append a value '[1]' to the empty list 'li'
        #append 'i' to the empty list 'li'
        #return list 'li'
    #if no
        #append a value '[1]' to the empty list 'li'
        #append 'i' to the empty list 'li'
        #reduce the value of 'numRows' by 2
        #while 'numRows' is greater than 0
            #initialize a list 'j' to with only one element '1'
            #initialize a variable 'indx' to 0
            #while 'indx' is less than 1 less than the value of length of the list 'i'
                #set a variable 'a' to sumation of value in list 'i' at index 'indx' and 'indx'+1
                #append the value of 'a' to list 'j'
                #increase the value of 'indx' by 1
            #append the value '1' to list 'j'
            #reassign the value of 'i' to 'j'
            #decrease the value of 'numRows' by 1
            #append 'j' to list 'li'
    #return 'li'

```
## Question: 9
### Leetcode 119: Pascal's Triangle II
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it

```

#Define getRow(rowIndex)
    #set variable 'i' to list [1,1]
    #Initialize a variable 'li' as empty list
    #check if 'rowIndex' is equal to 0
    #if yes
        #append a value '[1]' to the empty list 'li'
        #return the value of list 'li' at index 'rowIndex'
    #check if 'rowIndex' is equal to 1 
    #if yes
        #append a value '[1]' to the empty list 'li'
        #append 'i' to the empty list 'li'
        #return the value of list 'li' at index 'rowIndex'
    #if no
        #append a value '[1]' to the empty list 'li'
        #append 'i' to the empty list 'li'
        #set a new variable 'new_rowIndex' to 'rowIndex'
        #reduce the value of 'new_rowIndex' by 1
        #while 'new_rowIndex' is greater than 0
            #initialize a list 'j' to with only one element '1'
            #initialize a variable 'indx' to 0
            #while 'indx' is less than 1 less than the value of length of the list 'i'
                #set a variable 'a' to sumation of value in list 'i' at index 'indx' and 'indx'+1
                #append the value of 'a' to list 'j'
                #increase the value of 'indx' by 1
            #append the value '1' to list 'j'
            #reassign the value of 'i' to 'j'
            #decrease the value of 'new_rowIndex' by 1
            #append 'j' to list 'li'
    #return the value of list 'li' at index 'rowIndex'

```

## Question: 10
### Leetcode 121: Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

```

#Define maxProfit(prices)
    #set a variable 'min_value_indx' to 0
    #set a variable 'max_value_indx' to 1
    #Initialize an empty list 'profit1'
    #while the value of 'max_value_indx' less than or equal to value 1 less than the length of list 'prices'
        #set the variable 'min_value' to the value in list 'prices' at index 'min_value_indx'
        #set the variable 'max_value' to the value in list 'prices' at index 'max_value_indx'
        #check if 'min_value' is greater than 'max_value'
        #if yes
            #increase the value of 'min_value_indx' by 1
            #set 'max_value_indx' to 'min_value_indx' + 1
        #else check if 'min_value' is equal than 'max_value'
            #increase the value of 'min_value_indx' by 1
            #set 'max_value_indx' to 'min_value_indx' + 1
        #if no
            #initialize a variable 'profit2' to a value obtained by subtracting 'min_value' from 'max_value'
            #append the value of 'profit2' to 'profit1'
            #increase the value of 'max_value_indx'  by 1
    #check if list 'profit1' is empty
    #if yes
        #return 0
    #if no
        #return the max value in list 'profit1'
```

## Question: 11
### Leetcode 2460: Apply Operations to an Array 
You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:

If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
After performing all the operations, shift all the 0's to the end of the array.

For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
Return the resulting array.

```
First loop to check if nums[x] = nums[x+1] and if yes then replace value at index x with 0
second loop for checking if the value in list is 0 and if yes then removing that element and then appending it at the end
```

## Question: 12
### Leetcode 217: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

```
#Define the function:
    #sort the given array
    #Initialize pointer 1 to oth position
    #Intitialize pointer 2 to 1st position
    #loop till pointer 2 is at the last element
        #check if the value at pointer 1 is equal to the value at pointer 2
            #If yes return True
        #else Increase both pointer value by 1
    #if all the elements are unique then return false at the end

```
## Question: 13
### Leetcode 242: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

```
#Define the function:
    #sort string s
    #sort string t
    #return true if sorted string s is equal to sorted string t
    #or else return False

```

# 🧠 Single Number

**LeetCode Problem:** [Single Number](https://leetcode.com/problems/single-number/description/?envType=problem-list-v2&envId=array)

---

## 📘 Problem Description

You are given a **non-empty** array of integers `nums`, where every element appears **twice** except for **one**. Find and return the element that appears only **once**.

### Constraints:
- Each input will have exactly one element that appears once.
- All others appear exactly twice.
- Time complexity requirement: O(n)
- Space complexity: Can vary based on approach.

---

## 🧾 Example Input & Output

### Example 1:
**Input:**  
`nums = [2, 2, 1]`  
**Output:**  
`1`

### Example 2:
**Input:**  
`nums = [4, 1, 2, 1, 2]`  
**Output:**  
`4`

---

## ✅ Python Solution with Comments

```python
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









