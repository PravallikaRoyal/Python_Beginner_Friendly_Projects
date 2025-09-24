import random

#for generating password we need letters, numbers, symbols:
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',]

# Providing the choice for user to generate easy-level password or hard-level password:
choice = int(input("Enter 0 if you want to generate easy-level password, otherwise enter 1 if you want to generate hard-level password\n"))

print("Welcome to the Password Generator 😊")
no_of_letters = int(input("How many letters would you like to have in your password:"))
no_of_numbers = int(input("How many numbers would you like to have in your password:"))
no_of_symbols = int(input("How many symbols would you like to have in your password:"))

#Generating Easy - level Password:
if (choice == 0):
    password = ""
    for i in range(0,no_of_letters):
        password += random.choice(letters)
    
    for i in range(0, no_of_numbers):
        password += random.choice(numbers)
    
    for i in range(0, no_of_symbols):
        password += random.choice(symbols)
    
    print(password)

elif choice == 1:
    password_list = []
    for i in range (0, no_of_letters):
        password_list.append(random.choice(letters))

    for i in range (0, no_of_numbers):
        password_list.append(random.choice(numbers))
    
    for i in range (0, no_of_symbols):
        password_list.append(random.choice(symbols))
    
    password1 = ""
    random.shuffle(password_list)
    for i in password_list:
        password1 += i
    
    print(password1)
    
    



    


    


    


   




