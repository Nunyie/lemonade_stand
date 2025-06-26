# Nunyie
# Demonstrating the 4 Pillars of OOP through a lemonade stand simulation

print("Welcome to my Lemonade Stand")

class LemonadeStand:
    def purchase():
        print("Here is your lemonade!")

    def price():
        print("The price for 1 lemon is $0.50")

# Abstraction: This is where we hide the process of making lemonade from the user.
# The user only needs to know that they can purchase lemonade, not how it is made.

# LemonadeStand.purchase()

class Cashier(LemonadeStand):
    def __init__(self):
        self.__profit = 100 # Added 2 underscore to make the value private
    
    def total_order():
        print("Your total is $2.50")

    def price():
        print("The price for a Lemonade is $2.50")

    def profit(self):
        print("Total profit = ", self.__profit) # This method is used to access the private profit attribute

# Inheritance: Cashier is child class of LemonadeStand.
# It inherites the purchase() method from the LemonadeStand class. Which allows the cashier to call the purchase method since it is a subclass of LemonadeStand.

Cashier.price()
Cashier.purchase()
Cashier.total_order()

# Polymorphism: The price method in the LemonadeStand class is overridden in the Cashier class to provide a different price for lemonade.

# Encapsulation: The profit attribute in the Cashier class is private, meaning it cannot be accessed directly from outside the class.
# The public can no longer access the profit attribute directly, ensuring that the profit value is protected.
# Cashier = Cashier()
# print("Total profit = ", Cashier.__profit)
# print("Total profit = ", Cashier.__profit + 50)  # Adding $50 to the profit for demonstration

# To access the Total profit we call the profit method
Cashier = Cashier()
Cashier.profit()