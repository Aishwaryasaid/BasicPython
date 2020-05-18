# Dictionaries are key and value pairs
# key and value can be of any datatype
# Dictionaries are represented in {} brackets
# "key":"value"
# access the dict using dict_name["Key"]
student = {"name":"Jacob", "age":25,"course":["compsci","maths"]}
print(student["course"])

# use get method to inform user if a key doesn't exist in the dictionary
print(student.get("phone","Not Found!"))

# add the dictionary with new key value pair
student["phone"]:["555-000"]

# update as well as add the key value
student.update({'name':'jane', 'age':'18','address':'New Avenue Park,US'})

# delete the key
del student["name"]
print(student)

# In dictionary unlike list, pop takes the key as an argument to delete that specific key-value pair
student.pop("age")


# Access the key of dictionary
print(student.keys())

# Access the value of dictionary
print(student.values())




