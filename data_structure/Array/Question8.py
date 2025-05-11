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

# Use Case: 1 
# numRows = 5
# Output = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Expected = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Use Case: 2 
# numRows = 1
# Output = [[1]]
# Expected = [[1]]