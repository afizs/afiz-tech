dict_a = {
    "id": 10,
    "name": "Softdrinks",
    "price": 30,
}

dict_b = {
    "veg": True,
    "quantity": 1
}

# solution 1
dict_c = {**dict_a, **dict_b}
print(dict_c)

# solution 2
dict_a.update(dict_b)
print(dict_a)
