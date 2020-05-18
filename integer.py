#Arthimetic Operations

# Addition = 3 + 2
# Subtraction = 3 - 2
# Multiplication = 3 * 2
# Division = 3 / 2
# Floor Division = 3 // 2
# exponents = 3 ** 2
# Moduluos = 3%2

#PEMDAS(Paranthesis, Exponents, Multiplication, Division, Addition, Subtraction)

print(3 * (2+1))

#Absolute Value
print(abs(-1))

#round the value to near function

num = 3.75
print(round(num))

# add value to round that function to that value
print(round(num,1))

# Comparision Operator
# Equal 3==2
# Not Equal 3!=2
# Greater than 3>2
# Less than 3<2
# Greater or equal 3>=2
# Less or equal 3<=2

# It returns the boolean True or False

num_1 = 3
num_2 = 2
print(num_1 == num_2)


# a number can also be in the form of a string
num_1 = '300'
num_2 = '100'
print(num_1+num_2) #since it is in string format, it will concatanate two numbers

# Inorder to add them, cast them into int

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1+num_2)

#type function always you to check the type of a variable
print(type(num_1))

num_float = 3.75
# It can also cascade a float value
num = int(num_float)
print(num)


# round a floating point number
num_float = 3.75
print(round(num_float)) # it will round up the number

print(round(num_float,1)) # it will round the number upto one value
