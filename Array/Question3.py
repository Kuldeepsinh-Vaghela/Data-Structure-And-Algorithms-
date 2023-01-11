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
# Use Case: 1
# nums = [1,1,2]
# output = [1,2]

# Use Case: 2
# nums = [0,0,1,1,1,2,2,3,3,4]
# output = [0,1,2,3,4]

