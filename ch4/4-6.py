def square(x):
    '''与えられた数値の2条を返す'''
    return  x ** 2
print(square(10))

sq_func = lambda x: x**2
print(sq_func(10))

# range から数値のリストを作成し、文字列に変換して修飾します
i_num_list = range(1, 11)
s_num_list = list(map(lambda i: "No." + str(i), i_num_list))
print("文字列リスト:", s_num_list)

# 数値を文字に変換して修飾します
for s in map(lambda i: "No." + str(i), range(1, 11)):
    print(s, end=" ")


# 偶数だけ取得します
for e in filter(lambda x: x % 2 == 0, range(1, 11)):
    print(e, end=" ")

def is_even(x):
    # 偶数なら True を返します
    return x % 2 == 0

# 偶数だけ取得します
for e in filter(is_even, range(1, 11)):
    print(e, end=" ")


# 複数のペア要素を持つタプルからなるリスト
pairs = [(2, 'down'), (1, 'up'), (4, 'charm'), (3, 'strange'), (6, 'top'), (5, 'bottom')]

print("元のリスト:", pairs)

pairs.sort()
print(pairs)

pairs.sort(key=lambda x: x[1])
print(pairs)

pairs.sort(key=lambda x: x[1],reverse=True)
print(pairs)

n=3
func = lambda n: "even" if (n % 2 ==0) else "odd"

n = 3
x = "even" if (n % 2 == 0) else "odd"

n=3

if (n%2==0):
    x = "even"
else:
    x = "odd"
print(x)
