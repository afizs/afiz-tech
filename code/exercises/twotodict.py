keys = ['name', 'age', 'contact']
values = ['Afiz', 30, '9090909090']

# output: {'name': 'Afiz', 'age': 30, 'contact': '9090909090'}

print(dict(zip(keys, values)))

my_dictionary = {}

for i in range(len(keys)):
    my_dictionary[keys[i]] = values[i]

print(my_dictionary)


