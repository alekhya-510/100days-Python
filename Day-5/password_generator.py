import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=""

for char in range(0,nr_letters):
    password +=random.choice(letters)
for char in range(0,nr_symbols):
    password +=random.choice(symbols)
for char in range(0,nr_numbers):
    password +=random.choice(numbers)

print(password)

password1 =[]

for char in range(0,nr_letters):
    password1.append(random.choice(letters))
for char in range(0,nr_symbols):
    password1.append(random.choice(symbols))
for char in range(0,nr_numbers):
    password1.append(random.choice(numbers))

print(password1)
random.shuffle(password1)
print(password1)

final_pwd = ""
for char in password1:
    final_pwd += char
print("The final password is:" + final_pwd)

