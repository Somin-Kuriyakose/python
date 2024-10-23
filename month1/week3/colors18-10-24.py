user_input=input("Enter color names separated by commas:")
colors=user_input.split(',')
for i in range(len(colors)):
    colors[i]=colors[i].strip()
if colors:
    print("First color:",colors[0])
    print("Last color:",colors[-1])
else:
    print("No colors entered")
