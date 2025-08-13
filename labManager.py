# Author: Shasha Alvares
# Date: 2/24/25
# Description: Allow user to add, remove, or display equipment in the lab inventory or leave
# the program

#initialize empty lab list
lab = []
#boolean used to continue or end prompting user
cont = True

print("Welcome to the inventory manager for your laboratory!")
#display user options
while cont:
    print("\nYou can choose from the following options: "
          "\n1. Add Equipment "
          "\n2. Remove Equipment "
          "\n3. Display Current Equipment "
          "\n4. Leave the Laboratory Manager")

    userChoice = int(input("What would you like to do: "))

    #add equipment
    if userChoice == 1:
        #tell user lab is full
        if len(lab) == 5:
            print("Your laboratory cannot support any more equipment!")
        else:
            equipment = input("What would you like to add to the laboratory: ")
            lab.append(equipment)
            print(f"{equipment} has been added")
    #remove equipment
    elif userChoice == 2:
        equipment = input("What would you like to remove from the laboratory: ")
        if equipment in lab:
            lab.remove(equipment)
            print(f"{equipment} has been removed")
        else: #equipment not in lab
            print(f"{equipment} was not present and could not be removed")
    #display current equipment
    elif userChoice == 3:
        print("You're laboratory currently contains:", end=" ")
        for x in lab:
            print(x, end= ' ')
    #leave lab manager
    elif userChoice == 4:
        print("Good luck on your journey of discovery!")
        cont = False
   #let user know of invalid input
    else:
        print(f"{userChoice} was not a valid option. Please try again")