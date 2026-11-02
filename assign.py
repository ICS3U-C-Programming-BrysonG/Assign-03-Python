#!/usr/bin/env python3
# Created By: Bryson Grant
# Date: 11 02, 2026
# This program gets a pizza order from the user, and displays
# its cost back to them

import constants

def main():
    # Get size of pizza from the user
    pizza_size = input("Enter the size of pizza (1 = Small 2 = Medium" \
    " 3 = Large): ")

    try:
        pizza_size_int = int(pizza_size)
        if pizza_size_int == constants.SMALL:
            pizza_toppings = input("How many toppings do you want"
            " on your pizza (Max 4): ")
            if pizza_toppings == 1:
                toppings_price_small = pizza_toppings * constants.TOPPINGS_SMALL
            elif pizza_toppings == 2:
                toppings_price_small = pizza_toppings * constants.TOPPINGS_SMALL
            elif pizza_toppings == 3:
                toppings_price_small = pizza_toppings * constants.TOPPINGS_SMALL
            elif pizza_toppings == 4:
                toppings_price_small = pizza_toppings * constants.TOPPINGS_SMALL
            

        # Get amount of drinks from user
        amount_of_drinks = input("How many drinks do you want: ")
        try:
            amount_of_drinks_int = int(amount_of_drinks)
            if amount_of_drinks_int > 0:
                #Calculate cost of drinks
                cost_of_drinks = amount_of_drinks_int * constants.DRINKS
                # Calculate subtotal
                pizza_small_subtotal = constants.SMALL_COST + toppings_price_small + cost_of_drinks
            else:
                pizza_small_subtotal = constants.SMALL_COST + toppings_price_small
                # Calculate tax total
                pizza_small_tax_cost = pizza_small_subtotal * constants.HST
                # Calculate total cost of small pizza
                pizza_small_total_cost = pizza_small_subtotal + pizza_small_tax_cost
                # Display subtotal, tax and total cost of pizza to user
                print("The subtotal of your pizza and drinks is {:.2f}".format(pizza_small_subtotal))
                print("The total cost of tax is {:.2f}".format(pizza_small_tax_cost))
                print("The total cost of your pizza and drinks is {:.2f}".format(pizza_small_total_cost))
        except:
            print("{} is not a valid number".format(amount_of_drinks))
    except:
        print("{} is not a valid size".format(pizza_size))

if __name__ == "__main__":
    main()

