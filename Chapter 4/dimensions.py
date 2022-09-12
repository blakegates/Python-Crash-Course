# Tuples - lists that cannot change

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Changing item gives error:
# dimensions[0] = 250

# Loop through tuple
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions are:")
for dimension in dimensions:
    print(dimension)