#!/usr/bin/env python3
# Created By: Bryson Grant
# Date: 11 02, 2026
# This program gets a pizza order from the user, and displays
# its cost back to them

import constants


def main():
    # Get size of pizza from the user
    pizza_size = input("Hello, welcome to Brysons pizza shop! Enter the size of pizza (1 = Small 2 = Medium" " 3 = Large): ")
    # See if order inputted is a string
    try:
        pizza_size_int = int(pizza_size)
    except ValueError:
        print("{} is not a valid size".format(pizza_size))
    # Get number of toppings from the user
    pizza_toppings = input("How many toppings do you want on your pizza (Max 4): ")
    # See if order inputted is a string
    try:
        pizza_toppings_int = int(pizza_toppings)
    except ValueError:
        print("{} is not a valid number of toppings".format(pizza_toppings))
    # Get number of drinks from the user
    drinks = input("How many drinks do you want: ")
    # See if order inputted is a string
    try:
        drinks_int = int(drinks)
    except ValueError:
        print("{} is not a valid number of drinks".format(drinks))
    # Check if pizza size is small, and if the number of toppings is valid
    if pizza_size_int == constants.SMALL:
        if pizza_toppings_int >= 0 and pizza_toppings_int <= 4:
            toppings_price_small = pizza_toppings_int * constants.TOPPING_SMALL

            # Calculate price of drinks
            drinks_price = drinks_int * constants.DRINKS_COST
            # Calculate subtotal of the pizza
            pizza_small_subtotal = constants.SMALL_COST + toppings_price_small
            # Calculate tax total
            pizza_small_tax_cost = (pizza_small_subtotal + drinks_price) * constants.HST
            # Calculate total cost of small pizza
            pizza_small_total_cost = (
                pizza_small_subtotal + pizza_small_tax_cost + drinks_price
            )
            # Display subtotal, tax and total cost of pizza to user
            print("The subtotal of your pizza is ${:.2f}".format(pizza_small_subtotal))
            print("The subtotal of your drinks is ${:.2f}".format(drinks_price))
            print("The total cost of tax is ${:.2f}".format(pizza_small_tax_cost))
            print(
                "The total cost of your pizza and drinks is ${:.2f}".format(
                    pizza_small_total_cost
                )
            )


if __name__ == "__main__":
    main()
