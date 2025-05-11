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

# Use Case: 1
# nums = [1,3,5,6]
# target = 5
# Output = 2
# Expected = 2

# Use Case: 2
# nums = [1,3,5,6]
# target = 2
# Output = 1
# Expected = 1

# Use Case: 3
# nums = [1,3,5,6]
# target = 7
# Output = 4
# Expected = 4