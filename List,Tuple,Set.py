# List are written in [] brackets
# List can contain different datatypes like int, string, float
# List are mutable

courses = ["History","Physics","Maths","Science"]
print(courses[0]) # index value starts from Zero
print(courses[-1]) # last value of a list can be retrieved by -1

courses_1 = ["History", "Maths", "Science", "Compsci"]
courses_2 =["Art", "Education"]


# it will append a new list
courses_1.append(courses_2)
print(courses_1)

# it will insert a new list at that index value
courses_1.insert(0,courses_2)
print(courses_1)

# it will insert values of list2 in list1
courses_1.extend(courses_2)
print(courses_1)

# print the index value
courses = ["History","Physics","Maths","Science"]
print(courses.index('Science'))

# print the boolean value if that value is present in list
courses = ["History","Physics","Maths","Science"]
print('History'in courses)

# remove an item from the list using 'remove' method
courses.remove('Maths')
print(courses)

# using 'pop' method
courses.pop()
print(courses)

num = [5,3,4,1,2]
# use sort, sort will arrange numbers in ascending order
num.sort()
print(num)

# reverse using two ways
num.reverse()
print(num)

num_1 = [8,2,1,9,5,4,10,3,7,6]
num_1.sort(reverse=True)
print(num_1)

# you can slice a list and print sublist
alpha = ['a','b','c','d','e']
# startindex:endindex - it will not include the endindex
print(alpha[0:2])

# endvalue of a index can be printed using -1
print(alpha[-1])

# you can print the values by stepping the middle values
# if you want to print [a,c,e]
# startindex:endindex:step value -  step value specifices the indexvalue you wish to step

print(alpha[0:5])
print(alpha[0:5:2])

# print the list in reverse order
print(alpha[::-1])

# convert a list into a string
courses = ["History","Physics","Maths","Science"]
courses_str = ' - '.join(courses)
print(courses_str)

# *** Tuples ***
# tuples are immutable
# tuples are written in paranthesis
# tuple are ordered pair
# tuple can contain mix items of datatype

tuple1 = (1,'a')
print(tuple1[0])

# &&& Sets &&&
# Sets are written in curly brackets
# they are unordered and immutable
# sets throw away duplicate value
# every time a set is run, it changes the index of item in it

set1 = {"History","Maths","science","Algebra"}
print(set1)
set2 = {"Art","Education","Math","History"}
print(set2)
print(set1.difference(set2)) // set1 - set2
print(set2.difference(set1)) // set2 - set1
print(set1.union(set2))


# Empty List
empty_list = []
empty_list = list()

# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty set
empty_set = {} # this will create a dict
empty_set = set()