# Validating the email provided by user

# Taking input from user
email = input("Enter your email: ")
# Cleaning the email by trimming empty spaces from start and end 
email = email.strip()


# Email must not be empty
if email == "":
    print("Your email is empty! Please provide a valid email.")
# Email must contain . and @
elif not ('.' in email and '@' in email):
    print("Your email must conatin '.' and '@'")
# Email must not contain more than 1 @
elif email.count('@') != 1:
    print("Email should have only 1 @ symbol.")
# Email must end with .com, .org, or .net
elif not (email.endswith('.com') or email.endswith('.org') or email.endswith('.net')):
    print("Email must end with .com, .org or .net")
# Email must not be longer than 254 characters
elif len(email) > 254:
    print("Email must not be longer than 254 characters.")
# Email must have alphabet at start and end of it
elif not (email[0].isalpha and email[-1].isalpha):
    print("Email must start and end with alphabet")
else:
    print("Email is Valid")


 #################################################### ALTERNATE APPROACH ############################################################
# Note - If we will use if-elif-else statements then after encountering the very first issue our program will terminate and will not check for further issues. 
# So, if for example provided email is wasiq@@gmail.india then output will show issue of 2 "@" however there is another error which is email ends with .india
# Thus in order to rectify this issue we can use if-if-if statements.
# Example of that is below --: 


# Taking input from user
email2 = input("Enter your email: ")
valid = True
# Cleaning the email by trimming empty spaces from start and end 
email2 = email.strip()
# Email must not be empty
if email2 == "":
    print("Your email is empty! Please provide a valid email.")
    valid = False
# Email must contain . and @
if not ('.' in email2 and '@' in email2):
    print("Your email must conatin '.' and '@'")
    valid = False
# Email must not contain more than 1 @
if email2.count('@') != 1:
    print("Email should have only 1 @ symbol.")
    valid = False
# Email must end with .com, .org, or .net
if not (email2.endswith('.com') or email2.endswith('.org') or email2.endswith('.net')):
    print("Email must end with .com, .org or .net")
    valid = False
# Email must not be longer than 254 characters
if len(email2) > 254:
    print("Email must not be longer than 254 characters.")
    valid = False
# Email must have alphabet at start and end of it
if not (email2[0].isalpha and email2[-1].isalpha):
    print("Email must start and end with alphabet")
    valid = False
if valid:
    print("Email is Valid")