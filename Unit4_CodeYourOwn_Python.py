"""
Unit 4
Code Your Own: Unit 4
[Your Title Here]
"""
#library
import sys

### - - - Variables - - - ###

## - - Booleans - - ##
shopping = True
removal_process = False
show_reciept = True

## - - Lists - - ##
food_list_1 = ["Cherry Pie", "Loaf of Bread", "Ham"]
cost_part1 = [11.25, 9.50, 15.99] 

# - Empty Lists - #
cart = []
amount = []
total = 0


       
#Show the list of food and their cost using for in range loop with len(list)    
print("Here's a list of food to buy")

for i in range (len(food_list_1)):
    num_index = i + 1
    print(str(num_index) + ": " + str(food_list_1[i]) + " for $" + str(cost_part1[i]))
    

#Ask the user what they want to buy
while shopping == True:
    print()
    wanted_item = input("Enter 1, 2, 3, or done to proceed to checkout ")
    
    #Add an item to the lists cart and amount based on the user input
    if wanted_item == "1":
        cart.append(food_list_1[0])
        amount.append(cost_part1[0])
        total += cost_part1[0]

        
    if wanted_item == "2":
        cart.append(food_list_1[1])
        amount.append(cost_part1[1])
        total += cost_part1[1]

    if wanted_item == "3":
        cart.append(food_list_1[2])
        amount.append(cost_part1[2])
        total += cost_part1[2]
        
    print("Shopping Cart: " + str(cart))
    print("Total Cost: " + str(total)) 
    
    
    #If the user entered done end their shopping
    print()
    if wanted_item == "done":
        
        #Count how much the user has for each item using for-each loop
        for item in food_list_1:
            num_items = cart.count(item)
            print("You bought " + str(num_items) + " " + item)
            
        print("Total Cost: " + str(total))
        print()  
        
        #Ask the user if they want to remove any items
        remove_items = input("Do you want to remove any items? y/n ")
        if remove_items == "y":
            removal_process = True
                
        elif remove_items != "y":
            removal_process = False
            
        shopping = False
                
while removal_process:
    
    #Show the user's reciept using for in range
    print("Here is your reciept")
    for i in range (len(cart)):
        reciept_index = i + 1
        print(str(reciept_index) + ": " + str(cart[i]) + " for $" + str(amount[i]))
        print()
        
    #Ask the user what item they want to remove   
    item_remove = input("Enter the item number you want to remove or type done to checkout ")
    
    #If the user response is a digit remove that index from lists cart and amount
    if item_remove.isdigit():
        print("digit")
        item_index = int(item_remove) - 1
        del cart[item_index]
        del amount[item_index]
    else:
        #If user response is not a digit end the removal process
        removal_process = False

#If the removal_process is done exit the program            
else:
    print("Thank you for shopping with us!")
    sys.exit()
        
            





