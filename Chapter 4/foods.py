# Copying a list using [:]

my_foods = ['pizza', 'falfel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

for foods in my_foods:
    print(foods)

for foods in friend_foods:
    print(foods)