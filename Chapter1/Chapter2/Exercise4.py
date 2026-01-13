'''
Write  a  program  that  reads  in  numbers  separated  by  a  comma  in  one  line,  and  displays  distinct 
numbers  (i.e.,  if  a  number  appears  multiple  times,  it  is  displayed  only  once).  (Hint:  Read  all  the 
numbers and store them in list1. Create a new list list2. Add a number in list1 to list2. If the number is 
already in the list, ignore it.)
'''

# Ask the user to input numbers separated by commas
input_numbers = input("Enter some numbers separated by a comma: ").replace(" ", ",")

# Split the input string into a list of strings
number_strings = input_numbers.split(',')

number = []
for i in number_strings:
    number.append(int(i))
    
distinct_numbers =  sorted(set(number))
print("The distinct numbers are:", distinct_numbers)
