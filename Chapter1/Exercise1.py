# Write a program that calculate the energy needed to heat water from the initail temperature to a final temperature

# Ask the user to enter the value 
M = eval(input("Please enter the amount of the water in kg : "))

initial_temperature = eval(input("Please enter the initial temperature : "))

final_temperature = eval(input("Please enter the final temperature : "))

# Calculate the energy neede to heat 
Q = M * (final_temperature - initial_temperature)

#Print the result
print("The energy the that we needed to heat the water is = ", Q)
