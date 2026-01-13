'''
Write  a  program  to  display  all  open  locker  numbers  and  the  total  number of  open  lockers  when  the 
game ends. Hint: Use a list of 50 boolean elements, each of which indicates whether a locker is open 
(True) or closed (False).  
'''
# create 50 lockers, all closed (False)
lockers = [False] * 50

# players 1 to 50
for player in range(1, 51):

    #each player change locker that multiple f their numbber
    #i represent locker number from 1-50
    for i in range(player, 51, player):
        lockers[i-1] = not lockers[i-1]

#display open locker        
print (lockers)
for i in range(50):
    #if open true
    if lockers[i]:
        print(i+1,end=" ")

#total count locker are open
total_open = lockers.count(True)
print("Total open locker=" ,total_open)