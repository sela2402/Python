'''
Write a program that reads some integers between 1 and 100 separated by a comma in one line, and 
counts the occurrences of each.
'''

# Ask the user to input integers separated by commas
input_numbers = input("Enter some integers between 1 and 100 separated by a comma: ").replace(" ", ",")

# Split the input string into a list of strings
number_strings = input_numbers.split(',')
# Convert the list of strings to a list of integers
number_list = [int(num) for num in number_strings if num.isdigit() and 1 <= int(num) <= 100]
# Create a dictionary to count occurrences
occurrence_dict = {}    
for number in number_list:
    if number in occurrence_dict:
        occurrence_dict[number] += 1
    else:
        occurrence_dict[number] = 1
        
for number, count in occurrence_dict.items():
    if count > 1:
        print(f"{number} occurs {count} times")
    else:
        print(f"{number} occurs {count} time")