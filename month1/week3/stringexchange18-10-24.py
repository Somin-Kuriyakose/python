user_string=input("Enter a string:")
if len(user_string)>1:
    modified_string=user_string[-1]+user_string[1:-1]+user_string[0]
else:
    modified_string=user_string
print("Modified string:",modified_string)