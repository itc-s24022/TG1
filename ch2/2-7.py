[]
[2,4,8,16]
[2,4,8,16]+[3,6,9,12]
mylist = [2,4,8,16]
mylist + [3,6,9,12]
print(mylist)

my_list = [2, 4, 8, 16]
my_list.append(3)
my_list.append(6)
my_list.append(9)
print(my_list)

my_list = [2, 4, 8, 16]
my_list.extend([3, 6, 9, 12])
print(my_list)

my_list = [2, 4, 8, 16, 3, 6, 9, 12]
my_list.sort()
print(my_list)

my_list = [2, 4, 8, 16, 3, 6, 9, 12]
my_list.sort(reverse=True)
print(my_list)

my_list = [2, 4, 8, 16, 3, 6, 9, 12]
my_list.reverse()
print(my_list)

my_list = [2, 4, 8, 16, 3, 6, 9, 12]
my_list.sort()
my_list.reverse()
print(my_list)

my_list = [2, 4, 8, 16, 3, 6, 9, 12]
new_list = sorted(my_list)
rev_list = sorted(my_list, reverse=True)
print(my_list)
print(new_list)
print(rev_list)
