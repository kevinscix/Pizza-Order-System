# Name: Kevin Wu
# Student Number: 251284607

# Function that generates the receipt for the order of pizzas
def generateReceipt(pizzaOrder):
    # Checks if pizzas are ordered or empty order
    if len(pizzaOrder) == 0:
        print("You did not order anything")
    else:
        count = 0
        print("Your order:")
        price = 0
        # Loops through all the pizzas and prints them
        for i in pizzaOrder:
            count += 1
            pizzaToppings = i[1]
            toppingAmount = len(i[1])
            pizzaSize = i[0]
            pizzaPrice = 0
            extraToppingPrice = 0
            # Prices depending on the size of the pizza
            if pizzaSize == 'S':
                pizzaPrice = 7.99
                extraToppingPrice = 0.50
            elif pizzaSize == 'M':
                pizzaPrice = 9.99
                extraToppingPrice = 0.75
            elif pizzaSize == 'L':
                pizzaPrice = 11.99
                extraToppingPrice = 1.00
            elif pizzaSize == 'XL':
                pizzaPrice = 13.99
                extraToppingPrice = 1.25
            # Adds to the final price
            price += pizzaPrice
            # Print formatting for the type of pizza and its toppings
            print("Pizza {}: {}{:>21.2f}".format(count, i[0], pizzaPrice))
            for topping in pizzaToppings:
                print("- {}".format(topping))
            if toppingAmount > 3:
                for times in range(toppingAmount-3):
                    price += extraToppingPrice
                    print("Extra Topping ({}){:>14.2f}".format(pizzaSize, extraToppingPrice))
        # Prints the tax and the total amount
        print("Tax: {:>26.2f}".format(price*0.13))
        print("Total: {:>24.2f}".format((price*0.13) + price))
