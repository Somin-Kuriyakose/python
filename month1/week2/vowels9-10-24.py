str=input("Enter a string:")
vowels=["a","e","i","o","u","A","E","I","O","U"]
list=[]
for i in str:
    if(i in vowels):
        list.append(i)
if list:
    print("Vowels are:",list)
else:
    print("No vowels found")
