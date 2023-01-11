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
### Leetcode Que: 1
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

```

#Define twosum(nums,target)
    #for a value 'num' in the list 'nums'
        #find the index value of the 'num' and assign it to 'num_indx' variable
        #subtract 'num' from the 'target' and assign that value to 'lookup_num' variable
        #ignoring all the elements before 'num' and 'num' itself in the list 'nums', check if the 'lookup_num' variable value is present in the list 'nums'
        #if yes
            #find the index of the 'lookup_num' variable value in the list 'nums' where all the elements before 'num' and 'num' itself are sliced and assign it to 'lookup_num_index' variable
            #add 'num_indx', 'lookup_num_index' and 1 to get the real index of the 'lookup_num' variable value in list 'nums' 
            #print out 'num_indx' variable and the real index of the 'lookup_num' variable value in list 'nums' 
            #break the loop

```

## Question: 3


