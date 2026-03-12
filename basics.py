sample_lst = [1, 3, 4, 5, 3, 2, 1, 2, 3, 6, 2, 3]
count_dict = {}
for num in sample_lst:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
print(count_dict)
print("******************************************")
dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
# merged_dict={**dict1,**dict2}
dict1.update(**{"b":3,"c":4})
print(dict1)
print("******************************************")
lst1 = ["hi", 1, True]
new_lst = lst1*2
print(new_lst)
print("******************************************")
nums = [1, 2, 2, 3, 1]
u = dict.fromkeys(nums)
print(u)
unique = list(u)
print("******************************************")
nums = [1, 2, 2, 3, 3, 3, 4]
# most_common = max(set(nums), key=lambda x:x)
most_common = max(nums, key=nums.count)
print(most_common)
print("******************************************")
from collections import defaultdict
fruits_data = [('fruits', 'apple'), ('fruits', 'cherry'), ('vegetable', 'carrot'), ('cereals', 'lentil'), ('cereals', 'chickpeas')]
food_dict = defaultdict(list)
for category, item in fruits_data:
    food_dict[category].append(item)
print(food_dict)
print("******************************************")
my_set = set()
my_set.add(1)
# my_set.add([1, 2]) ----> error because set can contain only hashable objects (immutable)
print(my_set)
print("******************************************")
from collections import Counter
fruits_data = ['apple', 'cherry', 'strawberry', 'orange', 'apple', 'cherry']
counter = Counter(fruits_data)
print(counter)
print(counter["apple"])
print("************************************************")
scores = {"math": 90, "science": 80, "english": 95}
sorted_scores = sorted(scores.items(), key= lambda x: x[1])
print(sorted_scores)
print("************************************************")
words = ["listen", "silent", "enlist", "hello"]
words_dict = {"".join(sorted(word)) : [] for word in words}
for item in words:
    key_sorted = "".join(sorted(item))
    if key_sorted in words_dict:
        words_dict[key_sorted].append(item)
print(list(words_dict.values()))
print("************************************************")
input="abcd"
for index, character in enumerate(input):
    if character not in input[index + 1:]:
        break
print(character)
print("************************************************")
def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else: return fibonacci(n-1) + fibonacci(n-2)
print([fibonacci(n) for n in range(7)])
print("************************************************")
input = [1, 2, 3, 4, 5]
k=2
f = input[-k:] + input[:len(input) - k]
print(f)
s = f[-k:] + f[:len(f) - k]
print(s)
print("************************************************")
def check_balanced(input):
    stack = []
    mapping = { '}': '{' , ']': '[', ')': '('}
    for parenthesis in input:
        if parenthesis in '{([':
            stack.append(parenthesis)
        elif parenthesis in '}])':
            if not stack or stack[-1] != mapping[parenthesis]:
                return False
            stack.pop()
    return not stack
print(check_balanced(''))
print("************************************************")
def find_all_pairs_with_given_sum(target, int_arr):
    int_arr.sort()
    left_index = 0
    right_index = len(int_arr) - 1
    output = []
    while left_index < right_index:
        current_sum = int_arr[left_index] + int_arr[right_index]
        if current_sum == target:
            output.append((int_arr[left_index], int_arr[right_index]))
            left_index += 1
            right_index -= 1
            while left_index < right_index and int_arr[left_index] == int_arr[left_index + 1]:
                left_index += 1
            while left_index < right_index and int_arr[right_index] == int_arr[right_index - 1]:
                right_index -= 1
        elif current_sum <= target:
            left_index += 1
        else:
            right_index -= 1
    return output
print(find_all_pairs_with_given_sum(9, [1, 5, 2, 8, 3, 7, 4, 6, 4]))
print("************************************************")
def gen():
    for i in range(3):
        yield i
print(gen())
for val in gen():
    print(val)
print("************************************************")
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--name", default="guest")
args = parser.parse_args()
print(args.name)
print('********************************************************')
fruits = ['apple', 'watermelon', 'banana', 'cherry', 'kiwi', 'gauva', 'orange']
fruits.pop(1)
print(fruits)
print('********************************************************')
t1 = (1, 2, "hello")
t2 = (1, 2, "hello")
t3 = (1, 2, "world")

print(t1 is t2)       # True if tuple elemnts are immutable else false 
print(t1[2] is t2[2])  # True ("hello" string is interned)
print(t1[0] is t2[0])  # True (small integer 1 is interned)
empty_tuple=(9, [4, 5])
print(type(empty_tuple))
empty_tuple[1].append(6)
print(empty_tuple)
#indexing slicing concatenation * count index packing unpacking
mixed_tuple=(1,"Hello World",3.14, True)
print(mixed_tuple * 3)

my_set = {10, "hi", 2, 3, 4, 5, 6, 7, 9}
my_set.add(8)
print(my_set)
my_set.remove(5)
print(my_set)
my_set.discard(11)
print(my_set)
my_set.pop() #random
print(my_set)# sets can contain only hashable elements
#in membership tests

addition = lambda a, b: a+b
print(type(addition(1, 5)))
print(addition(1, 5))

dicti = {1:2, 2:3, 3:4, 4:5}
op = list(map(lambda k: k + dicti[k], dicti)) 
print(op)
#map needs a function first, then an iterable.
#dict.items() gives (key, value) pairs for iteration.
words = ['apple', 'banana', 'cherry']
print(list(map(str.upper, words)))
a = [1, 2, 3]
b = [4, 5, 6]
print(list(map(lambda x, y: x*y, a, b)))

even = list(filter(lambda x:x%2==0, range(10)))
print(even)

b = "$$$Cisco$Switch$$$" 
print(b.strip("$"))

#capitalize jfirst char (be it num or chhar) of the string, but title capitalises all words (first letter)
b = " 1cisco witch is coming"
print(b.capitalize())
print(b.title())

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
rem = crypto.pop(1) #based on key
print(crypto)
crypto.popitem() # removes last inserted
del crypto[3] #entire del also possible
print(crypto)

#range() in py3
# clear to empty

#positional parameters, default arguments, variable length tuple arguments, variable length keyword arguments

#The global keyword in Python is used inside a function to explicitly declare that a variable being assigned to is a global variable rather than a local one
#Case 1: Reading a global variable (no keyword needed)
#Case 2: Attempting to modify a global variable (without global)
#Case 3: Correctly modifying a global variable (with global)
#Case 4: Creating a new global variable inside a function
x = 10

def modify_x():
    # x = 5
    global x
    x = x + 5  # The following line will raise an UnboundLocalError: b4 making x as global
    print(x)


modify_x()
print(x)

class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p4 = None
    
    def square(self, p3):
        print(p3 ** 2)
 
p = ClassOne(1, 2)
 
setattr(p, 'p2', 50)
print(getattr(p, 'p4'))
print(hasattr(p, 'p4'))