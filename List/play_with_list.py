L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List:", L)

count = 0

# Finding the sum
for i in L:
    count += i

# Divide the total elements by the number of elements
avg = count/len(L)

print("Sum = ", count)
print("Average =", avg)

# Sorting the elements of the list
L.sort()

# Printing the first element
print("Smallest element is:", L[0])

# Printing the largest element
print("Largest element is:", L[-1])