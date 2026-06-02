import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = "!@#$%&*"

characters = lowercase+uppercase+numbers+special

length=int(input("How many characters should the password have?"))

if length<=0:
    print("password length cannot be lesser than or equal to 0")
else:
    password=""
    for i in range(length):
          random_character=random.choice(characters)
          password=password+random_character
          
    print("Generated password:",password)
