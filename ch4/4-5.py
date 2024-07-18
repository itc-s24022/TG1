sum([1,2,3,4])
sum(range(10))

add_all = sum
add_all([1,2,3,4])

add_all(range(10))

def say_hello():
    print('hello')
    
say_hello()

def run_any_func(func):
    for i in range(2):
       func()
       
run_any_func(say_hello)

def multi_func(number):
    if number == 0:
        print('min', end=" ")
        return min
    elif number == 1:
        print('max', end=" ")
        return max
    else:
        print('sum', end=" ")
        return sum

num_list = [1, 2, 3, 4]
for i in [0, 1, 2]:
    func = multi_func(i)
    print(func(num_list))

num_list = [1,2,3,4]
for i in [1,2,3]:
    print(multi_func(i)(num_list))
