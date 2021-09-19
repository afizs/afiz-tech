
### 1. Convert two lists into dictionary

`Input`: 
```python
keys = ['name', 'age', 'contact']
values = ['Afiz', 30, '9090909090']
```
`Output`: 
```python
{'name': 'Afiz', 'age': 30, 'contact': '9090909090'}
```
Source Code: 
```python
--8<-- "code/exercises/twotodict.py"
```
[YouTube](https://youtu.be/PFsP2U4_GH0)
### 2. Merge two dictionaries into one in Python

`input`: 
```python 
dict_a = {
    "id": 10,
    "name": "Softdrinks",
    "price": 30,
}

dict_b = {
    "veg": True,
    "quantity": 1
}
```
`output`: 
```
{
    "id": 10,
    "name": "Softdrinks",
    "price": 30,
    "veg": True,
    "quantity": 1
}
```
Source Code:
```python
--8<-- "code/exercises/mergetwo.py"
```
### 3. Create dictionary with default values

`input`: 
```python
items = ['Lemon rice', 'Paneer Masala', 'Parota']
defaults = {"veg": True,"quantity": 1 }
```
`output`: 
```python
{
    'Lemon rice': {"veg": True,"quantity": 1 }, 
    'Paneer Masala': {"veg": True,"quantity": 1 },
    'Parota': {"veg": True,"quantity": 1 }
}
```
Source Code: 
```python
--8<-- "code/exercises/default_values.py"
```
### 4. Create a new small dictionary from big dictionary

`input`: 
```python
dict_a = {
    "id": 10,
    "name": "Softdrinks",
    "price": 30,
    "veg": True,
    "quantity": 1
}

keys = ['id', 'name']
```
`output`: 
```python
{id: 10, name: softdrinks}
```
Source Code: 
```python
--8<-- "code/exercises/smallfrombig.py"
```
### 5. Delete set of keys from a dictionary

`input`: 
```python 
dict_a = {
    "id": 10,
    "name": "Softdrinks",
    "price": 30,
    "veg": True,
    "quantity": 1
}

keys_to_remove = ['veg', 'quantity']
```
`output`:
```python
{
    "id": 10,
    "name": "Softdrinks",
    "price": 30,
}
```
Source Code: 
```python
--8<-- "code/exercises/deletekeys.py"
```
### 6. Rename a key in the dictionary

`input`: 
```python
dict_a = {
    "id": 10,
    "name": "Softdrinks",
    "price": 30,
    "veg": True,
    "quantity": 1
}
# rename the "veg" key to "new_veg" 
```
output:
```python
dict_a = {
    "id": 10,
    "name": "Softdrinks",
    "price": 30,
    "new_veg": True,
    "quantity": 1
}
```
Source Code: 
```python
--8<-- "code/exercises/renamekey.py"
```
### 7. Get the key of a max value from a dictionary

`input`: 
```python 
scores = {
    "rohit": 76,
    'rahul': 45,
    'kohli': 43,
    'Jadeja': 89
}
```
`output`: `kohli`

Source Code: 
```python
--8<-- "code/exercises/getmax.py"
```
