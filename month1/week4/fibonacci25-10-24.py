n=int(input("Enter the number of term:"))
a=0
b=1
print("Fibonacci Series:")
for i in range(n):
    print(a,end="")
    a,b=b,a+b
