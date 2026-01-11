# Calculate:   1 - 2 + 3 - 4 + … + 29 - 30 

total = 0 
 
for i in range(1,31):
    if i % 2 == 0:
        total -= i
    else:
        total += i 
print("So 1 - 2 + 3 - 4 + … + 29 - 30 = ",total)