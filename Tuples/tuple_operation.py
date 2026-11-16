# Create an tuple with different datat types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

# Create a tuple
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)

# Adding new item to tuple
tuplex = tuplex + (9,)
print(tuplex)

# Counts the number of occurences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

# Create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 1, 6, 8)
_slice = tuplex[3:5]
print(_slice)
_slice = tuplex[:6]
print(_slice)