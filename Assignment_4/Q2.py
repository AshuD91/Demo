# Program to run repeated loops to determine the greatest among two entered numbers, 
# and then terminate the loop
while 1>0:
  
    print("lets play the game")
    print("Which is the greatest among two numbers")

    a=int(input("Enter the first number "))
    b=int(input("Enter the second number "))

    print("which is the greatest among two numbers")
    if a==b:
        print("The numbers are same")
    elif a>b:
        print("The greater number is ",a)
    else:
        print("The greater number is ",b) 
    
    print("---------------------")
    
    c=input("Enter the choice = done - to stop OR press 'any key' to continue ")
    
    if c=="done":
        print("END")
        exit()
    else:
        print("Starting the game again ")    
