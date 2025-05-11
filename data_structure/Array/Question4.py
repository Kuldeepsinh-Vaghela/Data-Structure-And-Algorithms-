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

# Use Case: 1
# nums = [3,2,2,3]
# val = 3
# Output = [2,2]
# Expected = [2,2]

# Use Case: 2
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# Output = [0,1,3,0,4]
# Expected = [0,1,4,0,3]