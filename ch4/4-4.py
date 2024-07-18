# グローバル変数を定義します
animal = 'cat'

# グローバル変数をプリントします
print("animal:", animal)

def my_func():
    # ローカル変数を定義します
    vegetable = 'carrot'
    
    # 関数の中でグローバル変数の値をプリントします
    print("animal inside function:", animal)
    # ローカル変数をプリントします
    print("vegetable:", vegetable)

my_func()

# グローバル変数を定義します
animal = 'cat'
print("animal:", animal)

def my_func():
    # ローカル変数を定義します
    vegetable = 'carrot'
    # 関数の中でグローバル変数の値をプリントします
    print("animal inside function:", animal)
    # ローカル変数をプリントします
    print("vegetable:", vegetable)

my_func()
# グローバル変数は変更されていない
print("animal after my_func:", animal)

animal = 'cat'
print("animal:", animal)

def my_func_alter():
    global animal
    animal = 'dog'
    print("animal in my_func_alter:", animal)

my_func_alter()
# グローバル変数が変更された
print("animal after my_func_alter:", animal)
