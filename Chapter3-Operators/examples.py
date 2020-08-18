# -*- coding: utf-8 -*-
separator = '----------------------------------------'

# Arithmetic Operators
print('Arithmetic Operators:')
a = 10
b = 5
print(f'a is {a}, b is {b}')

print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a ** b =', a ** b)
print('a // b =', a // b)
print('a % b =', a % b)

# Assignment Operators
# let us assign `c`, `d`, `e`, `f`, `g`, `h`, `i` all to 10
print(separator)
print('Assignment Operators:')
c = d = e = f = g = h = i = 10
print('c, d, e, f, g, h are all equals 10')

c += 2
print('c += 2, c is', c)

d -= 2
print('d -= 2, d is', d)

e *= 2
print('e *= 2, e is', e)

f /= 2
print('f /= 2, f is', f)

g **= 2
print('g **= 2, g is', g)

h //= 2
print('h //= 2, h is', h)

i %= 2
print('i %= 2, i is', i)


# Comparison Operators
# No examples!


# Logical Operators
# No examples too!


# Member Operators
print(separator)
print('Member Operators:')
j = 30
numbers = [10, 20, 30, 40, 50]

if j in numbers:
    print('`j` is in `numbers`')
else:
    print('`j` is not in `numbers`')


# Identity Operations
print(separator)
print('Identity Operations:')
k = [1, 2, 3]
m = n = [1, 2, 3]

print(m is n)
print(k is n)


# Bitwise Operators
print(separator)
print('Bitwise Operators:')
p = 10
q = 20
print(f'p is {p}, q is {q}')
print('p & q =', p & q)
print('p | q =', p | q)
print('~p =', ~p)
print('p ^ q =', p ^ q)
print('p << 2 =', p << 2)
print('q >> 2 =', q >> 2)
