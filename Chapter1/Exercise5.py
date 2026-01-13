# Wrtie the program to aks the user to guess the number
count = 0

# Create the variable 
computer_num = 50 

while True:
    # Ask the user to guess the number 
    User_guess = eval(input("Please guess the number : "))

    # Check the condition
    if User_guess > computer_num:
        print("The number is too high")
        count +=1 
    elif User_guess < computer_num:
        print("The number is too low")
        count +=1 
    else:
        print("Well done,you took" ,count, "attempts")
        break 