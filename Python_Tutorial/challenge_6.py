# Learning about Logical Operators

# 1: Check if username is not empty and the age is greater than or equals to 18
username = "wasiq"
age = 17

valid_credentials = (username != "" or username is not None) and age >= 18

# print(valid_credentials)

# 2: Check if the password is 8 characters long and does not contain blank spaces

password = "abcd1234"
blank_space = " "

is_valid = len(password) >= 8 and blank_space not in password

# print(is_valid)

# 3: Check if the user's email address is valid and contains @ and ends with .com
email = "wasiq_test@gmail.com"
special_char = "@"
domain = ".com"

is_acceptable = ((email != "" and email is not None) and special_char in email) and email.endswith(domain) 

# print(is_acceptable)

# 4: check if username is string, is not None and is longer than 5 characters
usersname = "wasiq0192"

is_correct = isinstance(usersname, str) and usersname is not None and len(usersname) > 5

print(is_correct)

if(is_correct):
    print("Your username is valid and acceptable")