#  Question 9
#  leet code 119: Pascal's Triangle II
#  Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

def getRow(rowIndex):
        i = [1,1]
        li = []
        if rowIndex == 0:
            li.append([1])
            return li[rowIndex]
        elif rowIndex == 1:
            li.append([1])
            li.append(i)
            return li[rowIndex]
        else:
            li.append([1])
            li.append(i)
            new_rowIndex = rowIndex
            new_rowIndex -= 1
            while new_rowIndex > 0:
                j=[1]
                indx = 0
                while indx < len(i)-1:
                    a = i[indx]+ i[indx+1]
                    j.append(a)
                    indx += 1
                j.append(1)
                i = j
                new_rowIndex -= 1
                li.append(j)
        return li[rowIndex]

# Use Case: 1
# rowIndex = 3
# Output = [1,3,3,1]
# Expected = [1,3,3,1]

# Use Case: 2
# rowIndex = 0
# Output = [1]
# Expected = [1]

# Use Case: 3
# rowIndex = 1
# Output = [1,1]
# Expected = [1,1]