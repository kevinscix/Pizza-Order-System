# Name: Kevin Wu
# Student Number: 251284607

# imports the pizza reciept function pizzaReceipt file
from pizzaReceipt import generateReceipt
# List of Toppings that can go on the pizza
TOPPINGS = ["ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE"]
# initializes the list for the pizzas to be appended into
pizzas = []
# gets the input for if they want a pizza
choice = input("Do you want to order a pizza? ").lower()
# IF empty immediately calls the receipt function
if choice == 'no' or choice == 'q':
    generateReceipt(pizzas)
# If anything else is typed it will ask for pizza size and generate a pizza to be put into the receipt
else:
    newPizza = True
    # Loops while they want to order pizza still
    while newPizza:
        currentPizza = []
        toppingCorrect = True
        # Loops while to make sure valid size is chosen
        while toppingCorrect:
            sizeChoice = input("Choose a size:  S, M, L, XL: ").upper()
            if sizeChoice == "S" or sizeChoice == "M" or sizeChoice == "L" or sizeChoice == "XL":
                toppingCorrect = False
                currentPizza.append(sizeChoice)
                addToppings = True
                toppingsOnPizza = []
                # Loops until no toppings want to be added
                while addToppings:
                    toppingChoice = input("Type in one of our toppings to add to your pizza. To see our list of toppings, enter 'LIST'. When done adding toppings, enter \"X\"\n").upper()
                    # Check if valid topping
                    if toppingChoice in TOPPINGS:
                        print("Added %s to your pizza" % toppingChoice)
                        toppingsOnPizza.append(toppingChoice)
                    # Check if want to end topping selection
                    elif toppingChoice == "X":
                        currentPizza.append(toppingsOnPizza)
                        pizzas.append(currentPizza)
                        # Check if they want more pizzas
                        continueOrder = input("Do you want to continue ordering? ").upper()
                        if continueOrder == "NO" or continueOrder == "Q":
                            addToppings = False
                            newPizza = False
                        elif continueOrder == "YES" or continueOrder == "Y":
                            addToppings = False
                    # Prints the list of toppings
                    elif toppingChoice == "LIST":
                        print("('ONION', 'TOMATO', 'GREEN PEPPER', 'MUSHROOM', 'OLIVE', 'SPINACH', 'BROCCOLI', "
                              "'PINEAPPLE', 'HOT PEPPER', 'PEPPERONI', 'HAM', 'BACON, 'GROUND BEEF', 'CHICKEN', "
                              "'SAUSAGE')")
                    else:
                        print("Invalid Topping")
    # Calls the receipt function
    generateReceipt(pizzas)
