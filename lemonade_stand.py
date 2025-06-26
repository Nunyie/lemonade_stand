# Nunyie
# Demonstrating the 4 Pillars of OOP through a lemonade stand simulation

print("Welcome to my Lemonade Stand")

class LemonadeStand:
    def purchase():
        print("Here is your lemonade!")

# Abstraction: This is where we hide the process of making lemonade from the user.
# The user only needs to know that they can purchase lemonade, not how it is made.

# LemonadeStand.purchase()

class Cashier(LemonadeStand):
    def total_order():
        print("Your total is $2.50")

Cashier.purchase()
Cashier.total_order()