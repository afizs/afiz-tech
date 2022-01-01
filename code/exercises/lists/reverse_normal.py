# input: [10, 20, 30, 40] ['Paddy', 'Ram', 'Bran', 'Andy']
# output: 10 Andy
#         20 Bran 

nums =  [10, 20, 30, 40]
names = ['Paddy', 'Ram', 'Bran', 'Andy']
for i in range(len(nums)):
    print(nums[i], names[len(names)-(i+1)])

print('--------')
for i, j in zip(nums, names[::-1]):
    print(i, j)