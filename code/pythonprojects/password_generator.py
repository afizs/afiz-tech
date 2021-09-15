import random
pass_len = int(input('enter the length: '))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?" 
password = ''.join(random.sample(s, pass_len))
print(password)
