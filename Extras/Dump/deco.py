def deco(func):
    def wrapper(x, y):
        x *= 10
        y *= 20
        return func(x, y)
    return wrapper

@deco
def add(x, y):
    return x+y

print add(1, 2)
print add(3, 4)



def add1(x, y):
    return x+y

add = deco(add1)
print '>>', add(1, 3)
