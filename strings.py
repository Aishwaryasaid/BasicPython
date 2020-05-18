# # store the message in a variable
# # variable name has to be in lowercase separated with "_"
# # variable name should be relevant to the context
# # Either use "" or ''
# my_message = "Hello World"
# my_message = 'Hello World'
#
# # two ways to add apostrotype in a string
# # first method
# my_message_1 = "Hi it's me"
# #print(my_message_1)
# # second method
# my_message_1 = 'Hi it\'s me'
# #print(my_message_1)
#
# # print more than one line using """ [3 double quotes]
# my_message = """
# Python is a high-level, interpreted, general-purpose programming language that supports
# both object-oriented programming and structured programming.
# It is quite versatile and offers a lot of functionalities using standard libraries which allows the
# easy implementation of complex applications.
# """
# #print(my_message)
#
# # find the length of a string
# #print(len(my_message))
#
# # convert it into uppercase
# #print(my_message.upper())
#
# # convert it into lowercase
# #print(my_message.lower())
#
# # count the number of words or number of letters
# #print(my_message.count("a"))
# #print(my_message.count("the"))
#
# my_message_2 = "Hello World"
#
# # find function returns the start of the index
# # print(my_message_2.find('World'))
# # find function returns -1 if that string is not available
# # print(my_message_2.find("Hi"))
#
# # replace function
# # it returns the replace value that needs to be stored in a variable and print
# message = "Hello World"
# message = message.replace("World","Universe")
# print(message)
#
# # 2 ways to concatenate two strings
# # first way
# greeting = "Hi"
# name = "Mitchell"
# #using + sign
# message = greeting + "," +name + "! Welcome."
# print(message)
#
# # second way - Formatted string
# message = '{},{}! Welcome.'.format(greeting,name)
# print(message)
#
# # f string format
# message = f'{greeting},{name}! Welcome.'
# #print(message)
#
# # dir method returns all the attributes and method of object name
# #print(help(dir(name)))
#
# # detail explaination of functions
# #print(help(str.lower))
#
# # Access the string with index position
# text = "Hi"
# #print(text[0])
#
# # Strings are immutable you cannot change the value with index position
# #text[0] = "p"
# #print(text[0]) # It will throw an error
#
# # an interger and a string can't be added using + sign, use "," instead
#
# str1 = "Hello"
# str2 = 3
#
#
# #print(a+b) # it will throw an error since we can't add a string and an integer
# # print(str1,str2) # use comma instead
#
# # string slicing - extract 0.8457
# # text = "X-DSPAM-Confidence:    0.8475";
# # text_find = text.find(':')
# # value = text[text_find+1:]
# # print(float(value))
# #
# #

