from functools import reduce
# what is the output of the following code?

numbers = {}

#dictory key must be immutable. In this case, tuple can be the key due to immutable feature.
numbers[(1,3,5)] = 2
numbers[(3,2,1)] = 6
numbers[(1,3)] = 10

sum = reduce(lambda x, y: x + y, numbers.values())

print(len(numbers) + sum)