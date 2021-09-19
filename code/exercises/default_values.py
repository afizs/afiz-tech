items = ['Lemon rice', 'Paneer Masala', 'Parota']
defaults = {"veg": True,"quantity": 1 }

# output: {'Lemon rice': {"veg": True,"quantity": 1 }, 
#           'Paneer Masala': {"veg": True,"quantity": 1 },
#           'Parota': {"veg": True,"quantity": 1 }}

my_dict = {}
for item in items:
    my_dict[item] = defaults

print(my_dict)

# solution 2 

my_dict_2 = dict.fromkeys(items, defaults)
print(my_dict_2)