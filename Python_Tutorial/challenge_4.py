#Learning about string Functions & Methods e.g. replace

#Convert the provided phone_num into all number e.g. 9999900000
phone_num = "+49 (176) 123-4567"
new_phone_num = phone_num.replace("+", "00").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")

print("Updated phone number is: ",new_phone_num)