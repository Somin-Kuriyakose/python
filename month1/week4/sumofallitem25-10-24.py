my_list=list(map(int,input("Enter number separated by spaces:").split()))
total=0
for item in my_list:
    total+=item
print("Sum of all items in the list:",total)
