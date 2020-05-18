# List Comprehension
# nums = [1,2,3,4,5,6,7,8,9,10]
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)
#
# my_list = [n for n in nums]
# print(my_list)

# Dictionary Comprehension

my_dict = {}
names = ['Bruce','Clark','Peter','Logan','Wade']
heroes = ['Batman','Superman','Spiderman','Wolverine','Deadpool']
a = zip(names,heroes)
print(list(a))
for name, hero in zip(names,heroes):
    print(name,hero)



