import random

# randomモジュールからrandintを使う
from random import randint
print(randint(0, 10))

# randomモジュールから複数の関数をインポートする
from random import randint, choice
print(randint(0, 10))
print(choice(['a', 'b', 'c']))

# randomモジュール全体を別名でインポートする
import random as rd
print(rd.randint(0, 10))

# 特定の関数を別名でインポートする
from random import randint as rint
print(rint(1, 10))

import sys
print(sys.path)