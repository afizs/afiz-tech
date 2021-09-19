# Delete set of keys from a dictionary
dict_a = {
    "id": 10,
    "name": "Softdrinks",
    "price": 30,
    "veg": True,
    "quantity": 1
}

keys_to_remove = ['veg', 'quantity']

total_keys = dict_a.keys()
my_dict = {key: dict_a[key] for key in total_keys - keys_to_remove}
print(my_dict)

# solution 2 
for key in keys_to_remove:
    dict_a.pop(key)

print(dict_a)