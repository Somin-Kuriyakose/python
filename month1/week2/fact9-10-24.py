n=int(input("Enter a limit:"))
fact=1
for lim in range(1,n+1):
    fact=fact*lim
print("Factorial of a",n,"is:",fact)
