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

# Use Case: 1
# digits = [1,2,3]
# Output = [1,2,4]
# Expected = [1,2,4]

# Use Case: 2
# digits = [4,3,2,1]
# Output = [4,3,2,2]
# Expected = [4,3,2,2]

# Use Case: 3
# digits = [9]
# Output = [1,0]
# Expected = [1,0]