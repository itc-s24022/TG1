if a >=10:
    print('OK')
else:
    print('NG')

a = 30
if a % 15 == 0:
    print('fifteen')
elif a % 3 == 0:
    print('three')
elif a % 5 == 0:
    print('five')
else:
    pass

a,b = 10,20
if a > 10 and b > 10:
    print('OK')
else:
    print('NG')

a,b = 20,10
if a > 10 and b > 10:
    print('OK')
else:
    print('NG')