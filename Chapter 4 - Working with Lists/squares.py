squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# More efficient
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# List comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)
squares = [value*7 for value in range(2, 15)]
print(squares)