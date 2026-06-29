# Convert the messy data in form of string to more organized data

string = "968-Maria, ( Data Engineer );; 27y  "

correct_string = string.strip().replace(";",",").replace("(", "",).replace(")","").lower()

extracted_name = correct_string[4:9]
extracted_role = correct_string[12:25]
extracted_age = correct_string[29:31]

print(f"name: {extracted_name} | role: {extracted_role} | age: {extracted_age}")