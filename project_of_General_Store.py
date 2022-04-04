sum = 0
while(True):
    userinput = input("Enter the item price or press q to quit :/n")
    userinput = 21
    if(userinput != 'q'):
        sum = sum + int(userinput)
        print(f"order total so far: {sum}")
    else:
        print(f"your Bill total is {sum} Thanks for shopping")
        break