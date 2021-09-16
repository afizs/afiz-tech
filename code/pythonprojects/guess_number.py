# Guess the number game
import random
number = random.randint(1, 10)

for i in range(1, 4):
    user = int(input('Guess the number: '))
    if user == number:
        print('Great!! You gusssed the number right')
        break
    else:
        print('sorry!! Incorrect guess')

print('Correct number is: ', number)