# Rename the key in the dictionary 

dict_a = {
    "id": 10,
    "name": "Softdrinks",
    "price": 30,
    "veg": True,
    "quantity": 1
}

dict_a['new_veg'] =  dict_a.pop('veg')

print(dict_a)