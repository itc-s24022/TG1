a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

a, b = b, a
print(a)
print(b)

d = (1, 2)
e, f = d
print(e)
print(f)

x = [10, 30]
y, z = x
print(y)
print(z)

p = (1, (10, 100))
q, (r, s) = p
print(q)
print(r)
print(s)

a, b, c = 1, 2.3, 'mojiretsu'
print(a)
print(b)
print(c)
