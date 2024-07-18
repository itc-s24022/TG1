for i in range(3):
    print("Hello world {}".format(i))
    
numbers = list(range(1,11))
print(sum(numbers))

g = 9.81

def my_function():
    """Explain how tp use "docstring"""
    pass

def my_fuction():
    """Explain how tp use "docstring"
    Do bothing but explain how use docstring.
    """
    pass

help(my_fuction)

print(my_fuction.__doc__)
