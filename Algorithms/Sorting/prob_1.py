# Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

# Example 1:

# Input:
# N = 5
# A[] = {1,2,3,5}
# Output: 4
# Example 2:

# Input:
# N = 10
# A[] = {6,1,2,8,3,4,7,10,5}
# Output: 9

# Your Task :
# You don't need to read input or print anything. Complete the function MissingNumber() that takes array and N as input  parameters and returns the value of the missing number.


# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)


# Constraints:
# 1 ≤ N ≤ 106
# 1 ≤ A[i] ≤ 106
##########################################################################################
def missingnumber(array,n):
    list_n_numbers = [x for x in range(1,n+1)]
    for value in list_n_numbers:
        if value not in  array:
            return value
    
    
array=[1,2,4,5]
n = 5

a = missingnumber(array=array,n=n)
print(a)

