# Ask the user to enter the names of three people they want to invite to a party and store them in a list.
name_list = []

name_invite =  input("The enter the name of the people that you want to invite: ").strip()

for name in name_invite.split(','):
    clean_name = name.strip()
    if clean_name and clean_name not in name_list:
        name_list.append(clean_name)
        
while True:
    add_name = input("Don you want to add more people to jion? (Yes or No): ").lower()
    
    if add_name == 'yes':
        new_name = input("Pleae enter the new name that you want to  invite: ").strip()
        if new_name and new_name not in name_list:
            name_list.append(new_name)
    elif add_name == 'no':
        break 
    else:
        print("Pleae to enter yes or no :")
        
print("The Name that You invited to the party:")
for index, name in enumerate(name_list, 1):
    print(f"{index}.{name.strip()}")