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


