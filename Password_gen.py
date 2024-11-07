import random

welcome = "This is a 'Password Generator' program."
print (welcome.center(75))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '$', '#', '%', '&', '*']

no_of_letters = int(input("Enter the number of letters: "))
password_list = []
for letter in range(1, no_of_letters+1):
    password_list.append(random.choice(letters))

no_of_numbers = int(input("Enter the total numbers you want: "))
for number in range(1, no_of_numbers+1):
    password_list.append(random.choice(numbers))

no_of_symbols = int(input("Enter the number of symbols: "))
for symbol in range(1, no_of_symbols+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ''
for character in password_list:
    password += character
print("Your password is: ",password) 