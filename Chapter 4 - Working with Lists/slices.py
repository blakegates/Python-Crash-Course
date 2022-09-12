# Slicing lists
pizzas = ['sausage', 'cheese', 'pepperoni']
for pizza in pizzas:
    print(f"My favorite pizza is {pizza}.")

print("\nThe first three items in the list are:")
print(pizzas[:3])

print("\nThe last three items in the list are:")
print(pizzas[0:])

print("\nThe middle item in the list is:")
print(pizzas[1:-1])