import random
import string

# variables for content of password
letters = string.ascii_letters
digits = string.digits
symbols = "~`! @#$%^&*()_-+={[}]|:;'<,>.?/"

# containers for contents and final password
signGroup = ""
Password = ""

# user input, length, what will password contain?
passLen = input("How long should the password be?: ")
WantLetters = input("should it contain letters?(y/n): ")
WantDigits = input("should it contain digits?(y/n): ")
WantSymbols = input("should it contain symbols?(y/n): ")

# check for answers and append contents to container accordingly
Questions = [WantLetters, WantDigits, WantSymbols]
Signs = [letters, digits, symbols]

for Question, Sign in zip(Questions, Signs):
    if Question == "y":
        signGroup += Sign

# ---------------------------------------------------------

# iterate "len" times, and append random character to final "Password" variable
for i in range(0, int(passLen)):
    letter = signGroup[random.randint(0, len(signGroup) - 1)]
    Password += letter

# output password to the user
print(Password)
