l = [1, 4, 5, 6, 7, 3, 5, 1, 3, 4, 5, 1]
count_dict={}
for num in l:
    if num in count_dict:
        count_dict[num] +=1
    else:
        count_dict[num] = 1
print(count_dict)
# print(count_dict.sort())
fruits=["apple","banana","cherry","kiwi","gauva"]
print(type(fruits))
print(fruits[-1:1:-1])
print(fruits[::-1])
print(fruits[::])
for index, fru in enumerate(fruits):
    print(index, fru)
new_list = [x**2 for x in range(10) if x>=5]
print(new_list)
pair = [(x,y) for x in new_list for y in fruits]
print(pair)
tup = (1,2,3,4,5)
rev = tup[::-1]
print(tup)
print(rev)
print(type(rev)) #slicing of tuple again results in a tuple
beg, *mid, end = tup
print(type(beg), beg)
print(type(mid), mid)
print(type(end), end) #unpacking using * returns different data type - list
my_set = {x for x in range(5)}
print(my_set)
s = {'name': 'Krish', 'age': 33, 'address': 'India'}
print(type(s.keys()))
print(s.keys())
print(type(s.items()))
print({x:x**2 for x in range(5)})
print(s.get('name', 'NA'))
print(s.get('mail', 'NA'))
s2 = {'mail': ['Krish@gmail.com'], 'height': 133, 'weight': 55}
s.update({"hi": 1, "hello": 2})
print(s)
print({**s, **s2}) #to create a new dictionary - dictionary unpacking, to preserve original dictionaries but it is again shallow copy
# s3 = s2 #1. = shallow copy
# s3 = {**s2} #2. shallw copy
# s3 = s2.copy() #3. shallow copy
# s3 = {k:v for k,v in s2.items()} # 4.shallow copy
import copy
s3 = copy.deepcopy(s2)

s3['height'] = '183cm'
s3['mail'].append('hi@gmail.com')
print(s2, s3)

addition=lambda a,b:a+b
print(type(addition))
print(addition(5,6))

even = lambda x: True if x%2 ==0 else False
print(even(100))

squares = list(map(lambda x:x**2, tup))
print(squares)
numbers1=[1,2,3]
numbers2=[4,5,6]
print(list(map(lambda x,y: x+y, numbers2, numbers1)))
str_numbers = ['1', '2', '3', '4', '5']
print(list(map(lambda x:int(x), str_numbers)))
print(list(map(str.upper, fruits)))
numbers=[1,2,3,4,5,6,7,8,9]
greater_than_five=list(filter(lambda x:x>5,numbers)) #fundamental difference between map and filter. check here
print(greater_than_five)

list_of_words = ['dusty', 'study', 'stone', 'tones']
anagram_dict = {''.join(sorted(word)): [] for word in list_of_words}
for word in list_of_words:
    if ''.join(sorted(word)) in anagram_dict:
        anagram_dict[''.join(sorted(word))].append(word)
print(anagram_dict.values())
scores = {"math": 90, "science": 80, "english": 95}
sorted_dict = sorted(scores, key=lambda x:scores[x], reverse=True)
print(sorted_dict)
fruits = ['apple', 'watermelon', 'banana', 'cherry', 'kiwi', 'gauva', 'orange']
fruits.pop(1)
print(fruits)
def quick_sort(arr):
    if len(arr) <= 1:
        # if the array contains 0 or 1 element, it's already sorted
        return arr
    pivot = arr[len(arr) // 2] # select a pivot as a middle element
    left = [x for x in arr if x < pivot] # elements less than `pivot`
    middle = [x for x in arr if x == pivot] # elements equal to `pivot`
    right = [x for x in arr if x > pivot] # elements larger than `pivot`
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([9, 7, 5, 11, 12, 2, 14, 3, 10, 6]))

# Outputs: [2, 3, 5, 6, 7, 9, 10, 11, 12, 14]