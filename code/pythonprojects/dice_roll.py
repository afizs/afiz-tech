# Dice roll simulator
import random

while True:
    print('1. Roll the dice\n2. Exit')
    choice = int(input())
    if choice == 1:
        num = random.randint(1, 6)
        print(f'Random number: {num}')
    else: 
        break