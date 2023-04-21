def outer(func):
    def inner(x, y):
       x = x*10
       y = y *10
       return func(x, y)
    return inner

def add1(x, y):
    return x+y

add = outer(add1)
print add(1, 3)
print add(2, 4)
print add(22, 3)
print add(1, 3)
