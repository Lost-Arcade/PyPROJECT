#PY-PASSWORD GENERATOR
import random as rd
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '$', '#', '%', '^', '&', '*', '(', ')', '_', '{', '}', '|']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters do you want in your password?\n"))
nr_numbers = int(input("How many numbers do you want in your password?\n"))
nr_symbol = int(input("How many symbols do you want in your password?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 numbers, 2 symbols : KutR10@*
Password = []
for char in range(0, nr_letters):
  Password.append(rd.choice(letters))

for char in range(0, nr_numbers):
  Password.append(rd.choice(numbers))

for char in range(0, nr_symbol):
  Password.append(rd.choice(symbols))
#print(Password)

#Hard Level - Order of character not randomised:
#e.g. 4 letter, 2 number, 2 symbol : Ku1tR@0*

Password_hard = []
for char in range(0, nr_letters):
  Password_hard.append(rd.choice(letters))

for char in range(0, nr_numbers):
  Password_hard.append(rd.choice(numbers))

for char in range(0, nr_symbol):
  Password_hard.append(rd.choice(symbols))
rd.shuffle(Password_hard)
#print(Password_hard)

password = ""
for char in Password_hard:
  password += char
print(f"Your hard password is {password}")

easy_password = ""
for char in Password:
  easy_password += char
print(f"Your easy password is {easy_password}")