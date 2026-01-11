# Write the program to calculate the area of Square and Triangle 

print("Please choise the option to calculate the area of the aquare of triangle")
print("1. Square")
print("2. Triangle")
option = input("Please choide the option : ")

if option == "1":
    print("Calculate the area of the square")
    length = eval(input("Please enter the length : "))
    area_square = pow(length,2)
    print("The area of the square is = ", area_square , " m^2")
elif option == "2":
    print("Calculate the area of triangle")
    base = eval(input("Enter the base : "))
    height = eval(input("Enter the height : "))
    area_triangle = 0.5 * base * height 
    print("The area of the triangle is = ", area_triangle," m^2")
else:
    print("Suitable error message.")