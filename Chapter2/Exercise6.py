# Write a program that stores five countries and their capital cities in a 2D list.  

countries_capitals = [
    ["Cambodia", "Phnom Penh"],
    ["China", "Beijing"],
    ["Japan", "Tokyo"],
    ["India", "Delhi"],
    ["Malaysia", "Kuala Lumpur"]
]

# Ask the users to guesss the capital city of each country
while True:
    score = 0
    for country, capital in countries_capitals:
        user_guess = input(f"What is the capital city of {country}? ").lower()
        if user_guess.strip().lower() == capital.lower():
            print("Correct! ✅")
            score += 1
        else:
            print(f"Incorrect! ❌ The capital city of {country} is {capital}.")

    print("The correct answers is : ", score)
    break