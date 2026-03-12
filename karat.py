'''
We are working on a security system for a badged-access room in our company's building.

Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:

1. All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)

2. All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)

Each collection should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it.

records1 = [
  ["Paul",     "enter"],
  ["Pauline",  "exit"],
  ["Paul",     "enter"],
  ["Paul",     "exit"],
  ["Martha",   "exit"],
  ["Joe",      "enter"],
  ["Martha",   "enter"],
  ["Steve",    "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Joe",      "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Joe",      "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Joe",      "enter"],
  ["Joe",      "enter"],
  ["Martha",   "exit"],
  ["Joe",      "exit"],
  ["Joe",      "exit"] 
]

Expected output: ["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline", "Curtis", "Joe"]

Other test cases:

records2 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]

Expected output: [], []

records3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]

Expected output: ["Paul"], ["Paul"]

records4 = [
  ["Raj", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
  ["Raj", "enter"],
]

Expected output: ["Raj", "Paul"], ["Paul"]

All Test Cases:
mismatches(records1) => ["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline", "Curtis", "Joe"]
mismatches(records2) => [], []
mismatches(records3) => ["Paul"], ["Paul"]
mismatches(records4) => ["Raj", "Paul"], ["Paul"]

n: length of the badge records array
'''
records1 = [
    ["Paul", "enter"],
    ["Pauline", "exit"],
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Martha", "exit"],
    ["Joe", "enter"],
    ["Martha", "enter"],
    ["Steve", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "enter"],
    ["Joe", "enter"],
    ["Curtis", "exit"],
    ["Curtis", "enter"],
    ["Joe", "exit"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "exit"],
    ["Joe", "enter"],
    ["Joe", "enter"],
    ["Martha", "exit"],
    ["Joe", "exit"],
    ["Joe", "exit"],
]
records2 = [
    ["Paul", "enter"],
    ["Paul", "exit"],
]
records3 = [
    ["Paul", "enter"],
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
]
records4 = [
    ["Raj", "enter"],
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
    ["Paul", "enter"],
    ["Raj", "enter"],
]
    
def get_collections(r):
    new_records = sorted(r, key=lambda x:x[0])
    names=set([x[0] for x in new_records])
    entry_collection, exit_collection = [], []
    for user in names:
        entries = [x for x in new_records if x[0]==user]
        stack = []
        for entry in entries:
            if entry[1] == 'enter':
                if not stack:
                    stack.append('enter')
                else:
                    entry_collection.append(entry[0])
            else:
                if not stack or stack[-1] != 'enter':
                    exit_collection.append(entry[0])
                else:
                    stack.pop()
        if stack:
            entry_collection.append(entry[0])
    return list(set(entry_collection)), list(set(exit_collection))    
    
    
    
    
# entry_collection, exit_collection = get_collections(records1)
# print(entry_collection, exit_collection)
from collections import defaultdict
def get_data(records):
    entries = defaultdict(list)
    for person, stamp in records:
        entries[person].append(stamp)
    people = entries.keys()
    print(people)
    entry_collection, exit_collection=[],[]
    for name, stamp in entries.items():
        stack = []
        for e in stamp:
            if e == 'enter':
                if not stack:
                    stack.append(e)
                else:
                    entry_collection.append(name)
            else:
                if stack and stack[-1]=='enter':
                    stack.pop()
                else:
                    exit_collection.append(name)
        if stack:
            entry_collection.append(name)
    print(list(set(entry_collection)), list(set(exit_collection)))
    # return entry_data, exit_data

# get_data(records1)
def check_parenthesis(par_str):
    ref_dict = {')':'(', '}': '{', ']': '['}
    check=True
    stack = []
    for c in par_str:
        if c in '([{':
            stack.append(c)
        else:
            if stack and stack[-1]==ref_dict[c]:
                stack.pop()
            else:
                check= False
    if stack:
        check= False
    return check
par_str = '({(][)})'
# print(check_parenthesis(par_str))

# Find the first non-repeating character
s = 'aaabbbccddde'
# for index, char in enumerate(s):
#     if char not in s[:index]+s[index+1:]:
#         output = char
#         break
unique = set(s)
print(unique)
output = [char for char in unique if s.count(char)==1][0]
print(output)

name='treesa angel george'
print(name.find('ge'))
from datetime import datetime, date
print(date.today())
now=datetime.now() #same as today()
print(now)
date_str = now.strftime('%Y-%m-%d')
print(date_str)
date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
print(date_obj)

pali = 'malayalam'
mid = len(pali)//2
print(mid)
print(pali[:mid+1])
print(pali[-1:-(mid+2):-1])
if pali[:mid+1] == pali[mid:][::-1]:
    print(True)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))