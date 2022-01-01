list_1 = ['app', 'bo', 'co', 'doc']
list_2 = ['le', 'y', 'ol', 'tor']

# output: ['apple', 'boy', 'cool', 'doctor']
list_3 = []
for i in range(len(list_1)):
    list_3.append(list_1[i]+list_2[i])

print(list_3)