def outer(a, b):
    print('outer function (a, b) = ({}, {})'.format(a, b))
    
    def inner(c, d):
        print('inner function (c, d) = ({}, {})'.format(c, d))
        return c * d
    
    return inner(a, b)

result = outer(4, 7)
print(result)


def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    
    return inner(saying)

result = knights('Ni!')
print(result)


def make_circle_area_func(pi=3.14):
    # 円の面積を計算する関数を作成する
    def circle_area(radius):
        '''円の面積を計算する'''
        return radius * radius * pi
    return circle_area

# piが初期設定 (3.14) のとき
circle_area_default = make_circle_area_func()

# piが 3.1415926535 のとき
circle_area_precise = make_circle_area_func(pi=3.1415926535)

# 半径2の円の面積、piの精度が異なる
print(circle_area_default(2))
print(circle_area_precise(2))


def show_message(num=0):
    """入力値に応じて違うメッセージを表示する"""

    def decolate(func):
        if num == 0:
            flag = "Red"
        else:
            flag = "Blue"

        print("==== flag:", flag)
        func()
        print("====")

    def show_selection():
        if num == 0:
            print("Selection is", num, "which may be the default")
        else:
            print("Your choice is", num)

    decolate(show_selection)

show_message(0)
show_message(1)
