from functools import reduce

# Map
numbers: list = [1, 2, 3, 4, 5]
squared: list = list(map(lambda x: x * 2, numbers))
print(squared)

# Filter
evens: list = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Zip
names: list = ["John", "Jane", "Mary"]
ages: list = [25, 26, 27]
zipList: list = list(zip(names, ages))
print(zipList)

# Reduce
numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum: int = reduce(lambda x, y: x + y, numbers)
print(sum)
