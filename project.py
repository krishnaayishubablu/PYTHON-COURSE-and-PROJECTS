# import random

# target = random.randint(1, 100)

# while True:
#     userChoice = int(input("Guess the target : "))
#     if(userChoice == target):
#         print("Sucess : Correct!!")
#         break

#     elif(userChoice < target):
#         print("your number was too small. Take a bigger guess..")
#     else:
#         print("your number was too big. Take a smaller guess..")



#     print("------- Game over--------")  


          #RANDOM PASSWORD GENERATOR

import random 
import string

pass_len = 4    
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValues)


print("your random password is:", password)    