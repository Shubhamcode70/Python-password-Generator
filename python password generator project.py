#Password Generator using python
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Python Password Generator")

letter_req = int(input("Enter the number of letter you want in your password :"))
symbol_req = int(input("Enter the number of symbol you want in your password :"))
number_req = int(input("Enter the number of digits you want in your password : "))

'''
#creating empty string with password name
password = ""

for letter in range(letter_req):
    password = password + random.choice(letters)
print(password)

for symbol in range(symbol_req):
    password = password + random.choice(symbols)
print(password)

for digit in range(number_req):
    password = password + random.choice(numbers)
print(password)
'''

#creating empty password list
password_list = []

for letter in range(letter_req):
    password_list.append(random.choice(letters))

    
for symbol in range(symbol_req):
     password_list.append(random.choice(symbols))


for digit in range(number_req):
   password_list.append(random.choice(numbers))
print(password_list)

#shuffling the list
random.shuffle(password_list)

#creating empty password string to store the elements from the list
password = ""
for chars in password_list:
    password = password + chars
print(password)