# from fastapi import FastAPI
# from fastapi.responses import Response
# from pydantic import BaseModel
# from typing import List

# import requests

# app = FastAPI()

# class User(BaseModel):
#     userId: int
#     id: int
#     title: str
#     body: str

# BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# @app.get("/")
# async def get_data():
#     response = requests.get(BASE_URL)
#     print(response.json())
#     return Response({"MSG": "Success"})

tup = (1,4,2,2,2)
count = [index for index, item in enumerate(tup) if item == 2]
count = tup.count(2)
print(count)

tup = tup*3
print(tup)

packed_tuple=1,"Hello",3.14
print(packed_tuple)
d = {'name': 24, 'age': 32}
print(d.get('names', 'nope'))

addition = lambda x, y : x+y
print(addition(2,3))

even = lambda x: x%2==0
print(even(10))
print(even(5))
numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x:x**3, numbers)))
print(list(map(lambda x,y: x+y, numbers, tup)))
print(list(map(lambda x,y,z: x*y*z, numbers, numbers, numbers)))

fruits = ['apple', 'watermelon', 'banana', 'banana', 'cherry', 'kiwi', 'gauva']
f = sorted(fruits, key=lambda x:x.count('n'), reverse=True)
print(f)
fruits.sort(reverse=True, key=len)
print(fruits)
num = [x for x in range(20)]
print(num)
lst1=[1,2,3,4]
lst2=['a','b','c','d']
print({k:v for k in lst1 for v in lst2})
print([(x, y) for x in lst1 for y in lst2])
print([(lst1[i], lst2[i]) for i in range(len(lst1))])
print([(val, lst2[i]) for i, val in enumerate(lst1)])

numbers=(1,2,3,4,5,6)
first,*middle,last=numbers
print(first)
print(middle)
print(last)

nested_tuple = ((1, 2, 3), ["a", "b", "c"], (True, False))
nested_tuple[1][0] = 'z'
print(nested_tuple)
# nested_tuple[1] = ['z'] //error

my_set={1,2,3,4,5, "0"}
# my_set={1,2,3,4,5, {"1":"0", "2":"0"}} //error: TypeError: unhashable type: 'dict'
my_set={1,2,3,4,5, (1, 2)} # no error
# my_set={1,2,3,4,5, (1, [2])}  //error :TypeError: unhashable type: 'list'
# my_set={1,2,3,4,5, "0", [1, 2, 3]} //error :TypeError: unhashable type: 'list'
print(my_set)

dict1={"a":1,"b":2}
dict2={"c":4}
dict1.update(**dict2)
print(dict1)
print(dict2)

addition=lambda a,b:a+b
type(addition)

from collections import defaultdict

def word_list(list_of_words):
    output = {''.join(sorted(word)):[] for word in list_of_words}
    for word in list_of_words:
        if "".join(sorted(word)) in output:
            output["".join(sorted(word))].append(word)
    return output.values() 
    
list_of_words = ['dusty',  'study', 'stone', 'tones']
out = {''.join(sorted(word)): [word] for word in list_of_words}
print(out.values())
# list_of_words= ['evil', 'vile', 'live', 'veil']
print(word_list(list_of_words)) 


memo = [0, 1]
n=5
# Loop from the 2nd index up to and including n
for i in range(2, n + 1):
    # Calculate the current Fibonacci number using the two preceding ones
    # already stored in the memo list.
    v = memo[i - 1] + memo[i - 2]
    memo.append(v)
print(memo)

s=''
for i in range(10):
    s+=str(i)
print(s)

class ProductNormal:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"ProductNormal(name={self.name!r}, price={self.price}, quantity={self.quantity})"

    def __eq__(self, other):
        if not isinstance(other, ProductNormal):
            return False
        return (self.name, self.price, self.quantity) == (other.name, other.price, other.quantity)

p1=ProductNormal("Laptop", 2345.45, 2)
p2=ProductNormal("Laptop", 2345.45, 2)
print(p1==p2) #True

from dataclasses import dataclass

@dataclass
class ProductData:
    name: str
    price: float
    quantity: int
p3=ProductNormal("Laptop", 2345.45, 2)
p4=ProductNormal("Laptop", 2345.45, 2)
print(p3==p4)
#The @dataclass decorator automatically generates __init__, __repr__, and __eq__ based on the type hints. 
"""
Why use frozen=True?
Safety: It prevents accidental bugs where data is modified unexpectedly in different parts of your code.
Hashability: Frozen dataclasses automatically generate a __hash__ method. This allows you to use the object as a key in a dictionary or store it in a set, which you cannot do with a normal mutable dataclass.
"""
from dataclasses import replace

# Create a new object based on p1 but with a different price
# p2 = replace(p1, price=1150.0)

# print(p1.price) # 1200.0 (unchanged)
# print(p2.price) # 1150.0 (new instance)
t1 = (1, 2, "hello")
t2 = (1, 2, "hello")
print(t1 is t2)  # This will be True because tuples are interned
t1 = (1, [2], "hello")
t2 = (1, [2], "hello")
print(t1 is t2)  # This will be False

def log(fn):
    def wrapper(*args, **kwargs):
        print(f'The function {fn.__name__} started execution!')
        return fn(*args, **kwargs) #positional arguments (*args) must come first, followed by keyword arguments (**kwargs).
    return wrapper

@log
def add(a:int, b:int)->int:
    return a+b
print(add(5,3))