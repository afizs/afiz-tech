# input: [1, 2, 3, 4, 5, 6, 7]
# output: [1, 4, 9, 16, 25, 36, 49]
a = [1, 2, 3, 4, 5, 6, 7]
b =  [num**2 for num in a]
print(b)