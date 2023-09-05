"""
Assignment #10, Part 1
Andrew Park
"""

#part a
def validate(prompt,datatype='float',low='unlimited',high='unlimited'):
    while True:
        userchoice = input(prompt)
        if datatype == 'float':
            try:
                userchoice = float(userchoice)
                if low != 'unlimited' and userchoice < low:
                    print('Invalid range, try again')
                elif high != 'unlimited' and userchoice > high:
                    print('Invalid range, try again')
                else:
                    return userchoice
            except ValueError:
                print('Not a number')
                
        elif datatype == 'integer':
            try:
                userchoice = int(userchoice)
                if low != 'unlimited' and userchoice < low:
                    print('Invalid range, try again')
                elif high != 'unlimited' and userchoice > high:
                    print('Invalid range, try again')
                else:
                    return userchoice
            except ValueError:
                print('Not a number')

#result1 = validate("Give me a float between 1 and 10: ", "float", 1, 10)
#print (result1)

inventory = {"onion rings": [1.29, 5], "small fries": [1.49, 20], "soft drink": [0.99, 10]}

while True:
    option = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
    #if user option is s
    if option == "s":
        item = input("Enter product name: ")
        #if the item is in the inventory, print the formatted item.
        if item in inventory:
            print("We sell", f"{item} at ${inventory[item][0]:.2f} per unit")
        else:
            print(f"Sorry, we don't sell {item}")
    #if user option is l
    elif option=="l":
        #format it to fit the given example. (Spacing and such)
        print('{:<20}{:<10}{}'.format('Product', 'Price', 'Quantity'))
        for x in inventory.keys():
            #format the pricing to the hunddreths
            price = '{:.2f}'.format(inventory[x][0])
            #match the format with the given above, product price quantity.
            print('{:<20}${:<10}{:<10}'.format(x, price, inventory[x][1]))

    #if user option is a
    elif option == "a":
        item = input("Enter a product name: ")
        if item in inventory:
            #if it's in, print that it's duplicate
            print("Duplicate product name")
        else:
            while True:
                #check if it's a float/valid input
                price = float(input("Enter a price: "))
                if price < 0:
                    print("Invalid range, try again.")
                else:
                    price = float(price)
                    break
                
            while True:
                #if it's not numeric or out of the range, error, if not, print the amount and add it to dictionary
                quantity = input("Enter an inventory amount: ")
                if not quantity.isnumeric() or int(quantity) < 0 or int(quantity) > 100:
                    print("Invalid input, try again.")
                else:
                    quantity = int(quantity)
                    break
                
            inventory[item] = [price, quantity]
            print("Product added")
    
    #if user option is r
    elif option == "r":
        item = input("Enter a product name: ")
        if item in inventory:
            #del removes the item from the dictionary
            del inventory[item]
            print("Product removed")
        else:
            print("Unknown product name")
    
    #if user option is u
    elif option == "u":
        item = input("Enter a product name: ")
        #check that it's in the inventory
        if item in inventory:
            update_choice = input("(n)ame, (p)rice, or (a)mount? ")
            if update_choice == "n":
                new_name = input("Enter a new name: ")
                #make sure it's not in because if it's already existing, it will replace it
                if new_name in inventory:
                    print("Product name already exists")
                else:
                    #remove the name from the dictionary and change it to th new one
                    inventory[new_name] = inventory.pop(item)
                    print("Product updated")
            elif update_choice == "p":
                while True:
                    price = float(input("Enter a new price: "))
                    if price < 0:
                        print("Invalid input, try again.")
                    else:
                        price = float(price)
                        break
                inventory[item][0] = price
                print("Product updated")
            elif update_choice == "a":
                while True:
                    quantity = input("Enter a new quantity: ")
                    if not quantity.isnumeric() or int(quantity) < 0 or int(quantity) > 100:
                        print("Invalid input, try again.")
                    else:
                        quantity = int(quantity)
                        break
                inventory[item][1] = quantity
                print("Product updated")
            else:
                print("Invalid input")
        else:
            print("Unknown product name")
            
                
    #if user option is e
    elif option == 'e':
        print()
        #set everything to a null state to compare
        low_price = high_price = None
        low_item = high_item = None
        total_cost = 0
        
        #total amount
        for item, (price, quantity) in inventory.items():
            total_cost += price * quantity
            
            #If low_price is None or prices of the items is lower than the current low_price, update the low_price and low_item variables
            #low price becomes when the prices are compared in the dictionary and same with high, looped comparison until
            #true low/high
            if low_price is None or price < low_price:
                low_price = price
                low_item = item
            #If high_price is None or prices of the items is higher than the current high_price, update the high_price and high_item variables
            if high_price is None or price > high_price:
                high_price = price
                high_item = item
        
        # Round the total cost, high price, and low price variables to 2 decimal places
        total_cost = round(total_cost, 2)
        high_price = round(high_price, 2)
        low_price = round(low_price, 2)
        
        # Print the total cost of all items in the inventory and the highest and lowest priced items
        print('Total cost of all items in the inventory: ${:.2f}'.format(total_cost))
        print('Highest priced item: ${:.2f} is {}'.format(high_price, high_item))
        print('Lowest priced item: ${:.2f} is {}'.format(low_price, low_item))
        print()


    elif option=='q':
        print('See you soon!')
        break
    else:
        print('Unknown command, try again')
