# replace 15 with 99 in the below list
# input: [5, 10, 15, 20, 25, 50, 20] 
# ouput: [5, 10, 99, 20, 25, 50, 20]

a = [5, 10, 88, 20, 25, 50, 20] 
if 15 in a:
    i = a.index(15)
    a[i] = 99

print(a)