"""Practice instantiating Pizza class"""

from lessons.pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True) # example of instantiation

sals_pizza: Pizza = Pizza("smal1", 2, False)

# def price(pizza_order: Pizza) -> float:
#     """Caluclate and return cost of pizza."""
#     cost: float = 2.0
#     if pizza_order.size == "large":
#         cost = 6.0
#     else:
#         cost = 5.0
#     # charge .75 per topping
#     cost += .75 * pizza_order.toppings
#     # charge $1 for gluten free
#     if pizza_order.gluten_free:
#         cost += 1.0
#     return cost

print(my_pizza.toppings)
print(my_pizza.price())
my_pizza.add_toppings(2) # my_pizza acts as self and add_toppings is what goes in the parentheses.
print(my_pizza.toppings)
print(my_pizza.price())