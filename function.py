def function():
    return "Hello World"


def function(greeting,name='you'):
    return f'{greeting},{name}'

print(function("Hello","Moses"))

# args takes argument, kwargs takes key argument
def my_func(*args,**kwargs):
    print(args)
    print(kwargs)


my_func('Math','Art', name='abc', Age = 25)
