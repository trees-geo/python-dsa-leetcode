def simple_generator():
    yield 1
    yield 2
    yield 3


gen = simple_generator()
for value in gen:
    print(value)

# Alternatively:
gen2 = simple_generator()
print(next(gen2))  # Output: 1
print(next(gen2))  # Output: 2
print(next(gen2))  # Output: 3
# print(next(gen2))  # StopIteration
print('*****************')
squares_generator = (x * x for x in range(5))
print(next(squares_generator))
print(next(squares_generator))
print(next(squares_generator))
print(next(squares_generator))
print(next(squares_generator))

# An iterable (list)
my_list = [1, 2, 3]

# Get an iterator from the iterable
my_iterator = iter(my_list)

# Use the iterator to get elements
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3

# Attempting to get the next element after exhaustion raises StopIteration
try:
    print(next(my_iterator))
except StopIteration:
    print("Iteration finished.")

"""
In Python, iterables are objects that can be iterated over, meaning you can traverse through their elements one by one. Examples include lists, tuples, strings, dictionaries, and sets. An object is considered an iterable if it implements the __iter__ method, which returns an iterator.
Iterators are objects that manage the state of an iteration. They are responsible for keeping track of the current position during iteration and providing the next item in the sequence. An object is considered an iterator if it implements both the __iter__ method (which returns self) and the __next__ method. The __next__ method returns the next item in the sequence and raises a StopIteration exception when there are no more items to return.
"""
