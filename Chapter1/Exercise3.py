# Write a program to display body mass index(BMI)

# Ask the user to enter the weight and height
weight = eval(input("Please input your weight in kg : "))
height = eval(input("Please input your hright in meters : "))

# Calculate the BMI 
BMI = weight / pow(height,2)

# Check the condition
if BMI <= 18.5:
    print("Underweight")
elif BMI < 24.9:
    print("Normal")
elif BMI <29.9:
    print("Overweight")
else:
    print("Obese")