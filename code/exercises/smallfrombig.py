# Create a new small dictionary from big dictionary 
dict_a = {
    "id": 10,
    "name": "Softdrinks",
    "price": 30,
    "veg": True,
    "quantity": 1
}

keys = ['id', 'name']
# {id: 10, name: softdrinks}
new_dict = {}
for key in keys:
    new_dict[key] =  dict_a[key]
print(new_dict)

# solution 2 
new_dict = {key: dict_a[key] for key in keys}
print(new_dict)