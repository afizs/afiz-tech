# remove all occurences of 99 in the below list
# input: [5, 99, 15, 20, 99, 50, 99]
# ouput: [5, 15, 20, 50,]

a = [5, 99, 15, 20, 99, 50, 99]

b = []

for num in a:
    if num != 99:
        b.append(num)

print(b)