# Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. 
# Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets 
# among M students such that :
# 1. Each student gets exactly one packet.
# 2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.
# Example 1:
# Input:
# N = 8, M = 5
# A = {3, 4, 1, 9, 56, 7, 9, 12}
# Output: 6
# Explanation: The minimum difference between maximum chocolates and minimum chocolates is 9 - 3 = 6 by
# choosing following M packets :{3, 4, 9, 7, 9}.
# Example 2:
# Input:
# N = 7, M = 3
# A = {7, 3, 2, 4, 9, 12, 56}
# Output: 2
# Explanation: The minimum difference between maximum chocolates and minimum chocolates is 4 - 2 = 2 
# by choosing following M packets :{3, 2, 4}.
# Your Task:
# You don't need to take any input or print anything. Your task is to complete the function findMinDiff() 
# which takes array A[ ], N and M as input parameters and returns the minimum possible difference between maximum number of 
# chocolates given to a student and minimum number of chocolates given to a student.
# Expected Time Complexity: O(N*Log(N))
# Expected Auxiliary Space: O(1)
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 105
# 1 ≤ Ai ≤ 109
# 1 ≤ M ≤ N
#############################################################################################################

def findMinDiff(A,N,M):
    j = 1
    while j <= len(A)-1:
        i = j-1
        value = A[j]
        while i > -1 and A[i] > value:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = value
        j += 1
    print(A)
    diff = 0
    l_p = 0
    r_p = M-1
    l_p_d = 0
    r_p_d = M-1
    while r_p_d <= len(A)-1:
        if l_p_d == 0:
            diff = A[r_p_d] - A[l_p_d]
            l_p_d += 1
            r_p_d += 1
            print(A[l_p:r_p+1])
        else:
            diff_2 = A[r_p_d] - A[l_p_d]
            if diff_2 < diff:
                diff = diff_2
                l_p = l_p_d
                r_p = r_p_d
                l_p_d += 1
                r_p_d += 1
                A[l_p:r_p+1]
    return A[l_p:r_p]


a = findMinDiff([3, 4, 1, 9, 56, 7, 9, 12],8,5)

print(a)
