# Get the key of a minimum value from a dictionary 
scores = {
    "rohit": 76,
    'rahul': 45,
    'kohli': 43,
    'Jadeja': 89
}

# output:  Kohli 
print(max(scores, key=scores.get))