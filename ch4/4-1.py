def my_func():
    pass

my_func()

def my_func(x):
    pass

my_func(1)

def my_func(x):
    return x

my_func('test')

def my_func(x):
    x.append(1)
    
    my_list = [0,1,2,3]
    my_func(my_list)
    my_list
    
    def my_func(x):
        result = [0]
        return result * x
    my_func(3)