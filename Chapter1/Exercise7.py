'''
Ask the user to enter their favorite color. If they enter “red”, “RED” or “Red” display the message “I 
like red too”, otherwise display the message “I don't like [color], I prefer red”. 
'''

# Ask the uer to enter their favorite from from color
Color = input("Please enter your favorite color : ")

if Color.lower() == "red":
    print("I like red too.")
else:
    print("I don't like ",Color, "I prefer red.")