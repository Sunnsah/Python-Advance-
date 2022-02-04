import random
import string


print("*** Welcome To Random Password Generator Websites for testing  ***")

characters = "abcdefghijklmnopqrstvxtz0123456789"

number = input("Enter the *Amount-of-PassWord* Do you need : ")
number = int(number)

length = input (" Enter the ----Length---- of Password: ")
length = int(length)

print(f"\n Here your Newly Created {number} password : ")


for pwd in range (number):
    passwords = " "

    for c in range (length):
        passwords += random.choice(characters)
             
        print(passwords)
