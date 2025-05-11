# Insertion Sort (inplace, no need for extras space)

list with A length

for j = 2 to A.length:
    # the value at jth position will be overwritten so storing it in a variable for future reference
    store_variable = A[j]
    # insert A[j] to sorted list A[1:j-1]
    # creating another pointer on the left side of pointer j
    i = j-1
    # looping to check all the values prior to pointer j and comparing them with the value at pointer j
    # checking if the value at i pointer is > value at j then shifting that value to j position
    while i > 0 and A[i]> store_variable:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = store_variable
