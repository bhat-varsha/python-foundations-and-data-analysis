import random
letter=['a' ,'b', 'c','d','e','f','g','h','i','j','k']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','%','$','^']

print("welcome to password generator")
no_letter=int(input("nop of letters u want in ur password?   "))
no_numbers=int(input("how many numbers u want?   "))
no_symbols=int(input("how many symbols u want?   "))

password_list=[]
for char in range(0,no_letter+1):
    password_list+=random.choice(letter)
for char in range(0,no_numbers+1):
    password_list+=random.choice(numbers)
for char in range(0,no_symbols+1):
    password_list+=random.choice(symbols)

random.shuffle(password_list)


password=""
for char in password_list:
    password+=char
print(f"ur pass word is {password}")